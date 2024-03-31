import json
import random
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash
from .topic_content import TopicContent
from .models import Post, Comment
from django.http import HttpResponse
from RestrictedPython import compile_restricted
from RestrictedPython.Guards import safe_builtins
from io import StringIO
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from contextlib import redirect_stdout
from .models import Note
from .forms import NoteForm
from django.views.decorators.http import require_POST


@require_POST
@login_required
def save_note(request):
    # Parse JSON data from the request body
    data = json.loads(request.body)
    form = NoteForm(data)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        # Return a success response along with the note's ID for future reference (e.g., deletion)
        return JsonResponse({"success": True, "message": "Note saved successfully.", "note_id": note.id})
    else:
        # Return an error response if the form is not valid
        return JsonResponse({"success": False, "message": "Failed to save the note."})
    
@login_required
def delete_note(request, note_id):
    try:
        note = Note.objects.get(id=note_id, user=request.user)
        note.delete()
        return JsonResponse({"success": True, "message": "Note deleted successfully."})
    except Note.DoesNotExist:
        return JsonResponse({"success": False, "message": "Note does not exist or could not be deleted."})



safe_builtins = {
    "print": print,
    "range": range,
    "len": len,
    "int": int,
    "float": float,
    "str": str,
    "list": list,
    "dict": dict,
    "set": set,
    "tuple": tuple,
    "abs": abs,
    "sum": sum,
    "min": min,
    "max": max,
    "round": round,
    "sorted": sorted,
}


# Optionally, add '__import__' functionality for specific safe imports
def safe_import(name, globals=None, locals=None, fromlist=(), level=0):
    allowed_modules = [
        "math",
        "datetime",
        "random",
        "os",
        "sys",
        "json",
        "time",
        "itertools",
        "collections",
    ]
    if name in allowed_modules:
        return __import__(name, globals, locals, fromlist, level)

    return __import__(name, globals, locals, fromlist, level)


@login_required(login_url="/login/")
def run_code(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        source_code = request.POST.get("code", "")
        points = request.POST.get("points")
        exoutput= request.POST.get("output")

        print("ppppppppppppppppppppppppppppp", points)
        # Redirect stdout to capture print statements
        buffer = StringIO()

        safe_builtins["__import__"] = safe_import

        exec_globalss = {
            "__builtins__": safe_builtins,
        }

        try:
            # Execute the user code with stdout redirected
            with redirect_stdout(buffer):
                exec(source_code, exec_globalss)

            output = buffer.getvalue()
            
            if exoutput.strip() == output.strip():
                user_profile.update_score_and_badge(int(points))

            if not output:
                output = "Program executed successfully, but no output was produced."

        except Exception as e:
            output = f"Error executing script: {str(e)}"

        return JsonResponse({"success": True, "output": output})
    else:
        score = user_profile.get_score()
        print("score ", score)
        return render(request, "code.html", {"score": score})


@login_required(login_url="login")
def chat(request):
    posts = Post.objects.all().order_by("-created_at")

    if request.method == "POST":
        if "postContent" in request.POST:
            post_content = request.POST.get("postContent")
            post = Post(author=request.user, content=post_content)
            post.save()
            return redirect("chat")
        elif "commentContent" in request.POST and "postId" in request.POST:
            comment_content = request.POST.get("commentContent")
            post_id = request.POST.get("postId")
            post = Post.objects.get(id=post_id)
            comment = Comment(post=post, author=request.user, content=comment_content)
            comment.save()
            return redirect("chat")

    return render(request, "chat.html", {"posts": posts})


# Create your views here.
@login_required(login_url="login")
def HomePage(request):
    return render(request, "home.html")


@login_required
def explanation(request, name):
    content = TopicContent(name).content
    notes = Note.objects.filter(user=request.user, topic=name)  # Query notes by topic
    return render(request, "explanation.html", {"content": content, "topic": name, "notes": notes})


@login_required(login_url="login")
def Quize(request,name):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        # Assuming the points are sent in the body of the POST request
        data = json.loads(request.body)
        points = data.get("points", 0)

        print("pointeeeeee=",points)
        # Update the score and level
        user_profile.update_score_and_badge(points)  # Ensure this method exists and properly updates the score and badge level

        # Redirect to the same view but with GET method to serve the updated quiz page
        return redirect(
            "leader_board"
        )  # 'quize' is the name of this view in your URLs configuration

    elif request.method == "GET":
        # Serve the quiz page based on current level and score
        progress_percentage = ((user_profile.score % 10) / 10) * 100
        context = {
            "score": user_profile.score,
            "badge_level": user_profile.badge_level,
            "progress_percentage": progress_percentage,
            "topic":name
        }
        # Dynamically select the template based on the user's badge level for GET requests
        template_name = f"quiz.html"
        return render(request, template_name, context)
    



def SignupPage(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect to home page if user is already logged in

    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")
    return render(request, "signup.html")


from django.contrib.auth import authenticate, login, logout


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("home")  # Redirect to home page if user is already logged in

    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request, "login.html", {"error": "Username or Password is incorrect!!!"}
            )
    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("login")


@login_required
def ProfilePage(request):
    return render(request, "profile.html")


@login_required
def update_password(request):
    if request.method == "POST":
        user = request.user
        old_pass = request.POST.get("old_pass")
        new_pass = request.POST.get("new_pass")
        confirm_pass = request.POST.get("c_pass")

        # Check if the new passwords match
        if new_pass != confirm_pass:
            return JsonResponse(
                {"success": False, "error": "New passwords do not match."}, status=400
            )

        # Verify old password
        if not user.check_password(old_pass):
            return JsonResponse(
                {"success": False, "error": "Incorrect old password."}, status=400
            )

        # Set new password
        user.set_password(new_pass)
        user.save()

        # Update session hash so the user doesn't get logged out
        update_session_auth_hash(request, user)

        return JsonResponse(
            {"success": True, "message": "Password updated successfully."}
        )

    # Non-POST request, or some other condition failed
    return JsonResponse(
        {"success": False, "error": "Invalid request method."}, status=405
    )


@login_required
def leader_board(request):
    # Retrieve user profiles ordered by score
    profiles = UserProfile.objects.order_by("-score")
    for profile in profiles:
        profile.is_current_user = request.user == profile.user
    # Pass profiles to the template
    return render(request, "leaderBoard.html", {"profiles": profiles})


@login_required
def game(request):
    puzzles = {
        "list_comprehension": [
            "# Generate squares of numbers 0 through 9",
            "squares = [x**2 for x in range(10)]",
            "print(squares)",
        ],
        "dictionary_comprehension": [
            "# Create a dictionary where the keys are numbers and the values are their squares",
            "squares_dict = {x: x**2 for x in range(5)}",
            "print(squares_dict)",
        ],
        "set_comprehension": [
            "# Generate a set of even numbers from 0 through 9",
            "evens = {x for x in range(10) if x % 2 == 0}",
            "print(evens)",
        ],
        "generator_expression": [
            "# Create a generator for even numbers",
            "even_gen = (x for x in range(10) if x % 2 == 0)",
            "for num in even_gen:",
            "    print(num)",
        ],
        "lambda_function": [
            "# A simple lambda function to add two numbers",
            "add = lambda x, y: x + y",
            "print(add(5, 3))",
        ],
        "map_usage": [
            "# Use map to convert strings to uppercase",
            "words = ['hello', 'world']",
            "upper_words = map(lambda x: x.upper(), words)",
            "print(list(upper_words))",
        ],
        "filter_usage": [
            "# Filter even numbers from a list",
            "numbers = range(10)",
            "even_numbers = filter(lambda x: x % 2 == 0, numbers)",
            "print(list(even_numbers))",
        ],
        "list_slice": [
            "# Reverse a list using slicing",
            "my_list = [1, 2, 3, 4, 5]",
            "reversed_list = my_list[::-1]",
            "print(reversed_list)",
        ],
        "try_except": [
            "# Basic try-except block",
            "try:",
            "    print(1/0)",
            "except ZeroDivisionError:",
            "    print('Cannot divide by zero')",
        ],
        "with_statement": [
            "# Using with statement for file operations",
            "with open('example.txt', 'w') as file:",
            "    file.write('Hello, world!')",
        ],
        "factorial": [
            "def factorial(n):",
            "    if n == 0:",
            "        return 1",
            "    else:",
            "        return n * factorial(n-1)",
            "print(factorial(5))",
        ],
        "fibonacci": [
            "def fibonacci(n):",
            "    if n <= 1:",
            "        return n",
            "    else:",
            "        return fibonacci(n-1) + fibonacci(n-2)",
            "print(fibonacci(10))",
        ],
        "sum_of_list": [
            "def sum_of_list(lst):",
            "    total = 0",
            "    for num in lst:",
            "        total += num",
            "    return total",
            "print(sum_of_list([1, 2, 3, 4, 5]))",
        ],
        "check_prime": [
            "def is_prime(n):",
            "    if n <= 1:",
            "        return False",
            "    for i in range(2, n):",
            "        if n % i == 0:",
            "            return False",
            "    return True",
            "print(is_prime(11))",
        ],
        "reverse_string": [
            "def reverse_string(s):",
            "    return s[::-1]",
            "print(reverse_string('hello'))",
        ],
        "recursive_fibonacci": [
            "def fibonacci(n):",
            "    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)",
            "print(fibonacci(10))",
        ],
        "decorator_example": [
            "def my_decorator(func):",
            "    def wrapper():",
            "        print('Something is happening before the function is called.')",
            "        func()",
            "        print('Something is happening after the function is called.')",
            "    return wrapper",
            "def say_hello():",
            "    print('Hello!')",
            "say_hello = my_decorator(say_hello)",
            "say_hello()",
        ],
        "class_example": [
            "class MyClass:",
            "    def __init__(self, name):",
            "        self.name = name",
            "    def say_hello(self):",
            "        print(f'Hello {self.name}')",
            "obj = MyClass('John')",
            "obj.say_hello()",
        ],
        "context_manager": [
            "class Open_File:",
            "    def __init__(self, filename, mode):",
            "        self.filename = filename",
            "        self.mode = mode",
            "    def __enter__(self):",
            "        self.file = open(self.filename, self.mode)",
            "        return self.file",
            "    def __exit__(self, exc_type, exc_val, traceback):",
            "        self.file.close()",
            "with Open_File('sample.txt', 'w') as f:",
            "    f.write('Hello, Python!')",
        ],
        "generator_function": [
            "def countdown(num):",
            "    while num > 0:",
            "        yield num",
            "        num -= 1",
            "for i in countdown(5):",
            "    print(i)",
        ],
        "list_flatten": [
            "def flatten(lst):",
            "    return [item for sublist in lst for item in sublist]",
            "print(flatten([[1, 2], [3, 4]]))",
        ],
        "dictionary_merge": [
            "dict1 = {'a': 1, 'b': 2}",
            "dict2 = {'b': 3, 'c': 4}",
            "merged_dict = {**dict1, **dict2}",
            "print(merged_dict)",
        ],
        "set_operations": [
            "set1 = {1, 2, 3}",
            "set2 = {3, 4, 5}",
            "union_set = set1 | set2",
            "intersection_set = set1 & set2",
            "difference_set = set1 - set2",
            "print(union_set, intersection_set, difference_set)",
        ],
        "file_reading": [
            "with open('sample.txt', 'r') as file:",
            "    content = file.read()",
            "    print(content)",
        ],
        "comprehension_conditional": [
            "numbers = [1, 2, 3, 4, 5, 6]",
            "even_squares = [x**2 for x in numbers if x % 2 == 0]",
            "print(even_squares)",
        ],
    }

    # Select one random list from the puzzles
    random_key = random.choice(list(puzzles.keys()))
    code_snippets = puzzles[random_key]

    # Generate a list of indices and shuffle it
    indices = list(range(len(code_snippets)))
    random.shuffle(indices)

    # Pair each shuffled index with its snippet
    shuffled_snippets_with_indices = [
        (index, code_snippets[index]) for index in indices
    ]
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Assuming the points are sent in the body of the POST request
        data = json.loads(request.body)
        points = data.get("points", 0)
        print("Score Updted Bu Game", points)

        # Update the score and level
        user_profile.update_score_and_badge(points)

    progress_percentage = ((user_profile.score % 10) / 10) * 100
    print("pppppppppppppppp", progress_percentage)
    return render(
        request,
        "game.html",
        {
            "snippets_with_indices": shuffled_snippets_with_indices,
            "hint": random_key,
            "score": user_profile.score,
            "badge_level": user_profile.badge_level,
            "progress_percentage": progress_percentage,
        },
    )


@login_required
def gameTopic(request, topic_name):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        # Assuming the points are sent in the body of the POST request
        data = json.loads(request.body)
        points = data.get("points", 0)
        print("Score Updted Bu Game", points)

        # Update the score and level
        user_profile.update_score_and_badge(points)

    if topic_name == "Control Structures":
        puzzles = {
    "simple_if_statement": [
        "# Create a basic 'if' statement to check a condition:",
        "a = 10",
        "print('Value of a is:', a)",
        "if a > 5:",
        "    print('a is greater than 5')"
    ],
    "counting_while_loop": [
        "# Implement a 'while' loop to count from 0 to 4:",
        "count = 0",
        "while count < 5:",
        "    print('Count is:', count)",
        "    count += 1"
    ],
    "iterate_list_for_loop": [
        "# Iterate through a list and print each element using a 'for' loop:",
        "fruits = ['apple', 'banana', 'cherry']",
        "for fruit in fruits:",
        "    print(fruit)"
    ],
    "nested_if_statements": [
        "# Construct nested 'if' statements to check multiple conditions:",
        "x = 10",
        "if x > 5:",
        "    if x < 15:",
        "        print('x is between 5 and 15')"
    ],
    "iterate_dict_for_loop": [
        "# Iterate through a dictionary and print key-value pairs using a 'for' loop:",
        "my_dict = {'apple': 5, 'banana': 10, 'cherry': 15}",
        "for key, value in my_dict.items():",
        "    print(key, value)"
    ],
    "check_odd_even_while_loop": [
        "# Use a 'while' loop to identify and print odd or even numbers from 0 to 4:",
        "count = 0",
        "while count < 5:",
        "    if count % 2 == 0:",
        "        print(count, 'is even')",
        "    else:",
        "        print(count, 'is odd')",
        "    count += 1"
    ],
    "check_number_and_print": [
        "# Check a number and print a message based on its value using an 'if-else' block:",
        "x = 5",
        "if x > 10:",
        "    print('x is greater than 10')",
        "else:",
        "    print('x is not greater than 10')"
    ],
    "iterate_string_for_loop": [
        "# Iterate through a string and print each character using a 'for' loop:",
        "my_string = 'Python'",
        "for char in my_string:",
        "    print(char)"
    ]
}



    elif topic_name == "Inheritance":
        puzzles = {
    "define_class_attributes_methods": [
        "# Arrange the following code snippets in the correct order to define a Python class with attributes and methods:",
        "class Person:",
        "    def __init__(self, name, age):",
        "        self.name = name",
        "        self.age = age",
        "    def __str__(self):",
        "        return f'Name: {self.name}, Age: {self.age}'",
        "    def get_age(self):",
        "        return self.age"
    ],
    "create_instance_and_print_details": [
        "# Arrange the following code snippets in the correct order to create an instance of the class defined in the previous question and print its details:",
        "from person_class import Person",
        "person = Person('John', 30)",
        "print(person)"
    ],
    "define_recursive_factorial_function": [
        "# Arrange the following code snippets in the correct order to define a function in Python that calculates the factorial of a number recursively:",
        "def factorial(n):",
        "    if n == 0:",
        "        return 1",
        "    return n * factorial(n-1)"
    ],
    "sort_list_ascending_order": [
        "# Arrange the following code snippets in the correct order to define a list of numbers and sort it in ascending order using the sorted() function:",
        "numbers = [4, 2, 7, 1, 5]",
        "sorted_numbers = sorted(numbers)",
        "print(sorted_numbers)"
    ],
    "print_dict_keys_in_alphabetical_order": [
        "# Arrange the following code snippets in the correct order to define a Python dictionary and print its keys in alphabetical order:",
        "d = {'b': 2, 'a': 1, 'c': 3}",
        "print(sorted(d.keys()))"
    ],
    "define_rectangle_area_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that calculates the area of a rectangle:",
        "def area_rectangle(length, width):",
        "    return length * width"
    ],
    "define_class_with_class_variable_method": [
        "# Arrange the following code snippets in the correct order to define a Python class with a class variable and a method to access it:",
        "class MyClass:",
        "    class_variable = 10",
        "    @classmethod",
        "    def get_class_variable(cls):",
        "        return cls.class_variable"
    ],
    "generate_fibonacci_numbers": [
        "# Arrange the following code snippets in the correct order to define a Python generator function that generates Fibonacci numbers:",
        "def fibonacci():",
        "    a, b = 0, 1",
        "    while True:",
        "        yield b",
        "        a, b = b, a + b"
    ],
    "check_prime_number_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that checks if a given number is prime:",
        "def is_prime(num):",
        "    if num < 2:",
        "        return False",
        "    for i in range(2, int(num**0.5) + 1):",
        "        if num % i == 0:",
        "            return False",
        "    return True"
    ],
    "calculate_cylinder_volume_method": [
        "# Arrange the following code snippets in the correct order to define a Python class with a method to calculate the volume of a cylinder:",
        "class Cylinder:",
        "    def __init__(self, radius, height):",
        "        self.radius = radius",
        "        self.height = height",
        "    def calculate_volume(self):",
        "        return 3.14 * self.radius ** 2 * self.height"
    ],
    "sort_strings_by_length_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that sorts a list of strings by their lengths:",
        "def sort_by_length(strings):",
        "    return sorted(strings, key=len)"
    ],
    "remove_duplicates_from_list_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that removes duplicate elements from a list:",
        "def remove_duplicates(lst):",
        "    return list(set(lst))"
    ],
    "calculate_sum_of_list_elements_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that calculates the sum of elements in a list:",
        "def sum_elements(lst):",
        "    return sum(lst)"
    ],
    "check_palindrome_string_function": [
        "# Arrange the following code snippets in the correct order to define a Python function that checks if a given string is a palindrome:",
        "def is_palindrome(s):",
        "    return s == s[::-1]"
    ],
    "calculate_factorial_iteratively": [
        "# Arrange the following code snippets in the correct order to define a Python function that calculates the factorial of a number iteratively:",
        "def factorial(n):",
        "    result = 1",
        "    for i in range(1, n + 1):",
        "        result *= i",
        "    return result"
    ]
}



    elif topic_name == "Arrays":
        puzzles = {
    "create_and_access_array": [
        "# Arrange the following code snippets in the correct order to create an array of integers and access an element:",
        "import array",
        "arr = array.array('i', [1, 2, 3, 4, 5])",
        "print(arr[0])  # Output: 1"
    ],
    "insert_and_delete_element": [
        "# Arrange the following code snippets in the correct order to insert and delete an element from the array:",
        "arr.insert(2, 6)  # Insert 6 at index 2",
        "arr.remove(3)  # Remove the first occurrence of 3"
    ],
    "concatenate_and_print_array": [
        "# Arrange the following code snippets in the correct order to concatenate two arrays and print the result:",
        "arr2 = array.array('i', [7, 8, 9])",
        "arr += arr2",
        "print(arr)  # Output: array('i', [1, 2, 6, 4, 5, 7, 8, 9])"
    ],
    "create_string_array": [
        "# Arrange the following code snippets to create an array of strings:",
        "str_array = array.array('str', ['apple', 'banana', 'cherry'])"
    ],
    "slice_and_print_array": [
        "# Arrange the following code snippets in the correct order to slice an array and print the result:",
        "print(arr[2:5])  # Output: array('i', [6, 4, 5])"
    ],
    "update_element_in_array": [
        "# Arrange the following code snippets in the correct order to update an element in the array:",
        "arr[1] = 10  # Update the element at index 1 to 10"
    ],
    "find_index_of_element": [
        "# Arrange the following code snippets in the correct order to find the index of an element in the array:",
        "index = arr.index(4)  # Find the index of element 4"
    ],
    "reverse_and_print_array": [
        "# Arrange the following code snippets in the correct order to reverse the array and print the result:",
        "arr.reverse()  # Reverse the array",
        "print(arr)  # Output: array('i', [5, 4, 6, 2, 1])"
    ],
    "get_array_length": [
        "# Arrange the following code snippets in the correct order to get the length of the array:",
        "length = len(arr)  # Get the length of the array"
    ],
    "remove_all_elements": [
        "# Arrange the following code snippets in the correct order to remove all elements from the array:",
        "arr.clear()  # Remove all elements from the array"
    ]
}
    
    elif topic_name == "Data Types":
        puzzles = {
    "define_string_variable": [
        "# Rearrange the following code blocks to define a string variable and print it:",
        "input_string = 'Hello, World!'",
        "print(input_string)"
    ],
    "define_integer_variable": [
        "# Rearrange the following code blocks to define an integer variable and print it:",
        "my_integer = 42",
        "print(my_integer)"
    ],
    "define_float_variable": [
        "# Rearrange the following code blocks to define a float variable and print it:",
        "my_float = 3.14",
        "print(my_float)"
    ],
    "define_boolean_variable": [
        "# Rearrange the following code blocks to define a boolean variable and print it:",
        "is_valid = True",
        "print(is_valid)"
    ],
    "define_list_variable": [
        "# Rearrange the following code blocks to define a list variable and print it:",
        "my_list = [1, 2, 3, 4, 5]",
        "print(my_list)"
    ],
    "define_tuple_variable": [
        "# Rearrange the following code blocks to define a tuple variable and print it:",
        "my_tuple = (1, 2, 3, 4, 5)",
        "print(my_tuple)"
    ],
    "define_dictionary_variable": [
        "# Rearrange the following code blocks to define a dictionary variable and print it:",
        "my_dict = {'name': 'John', 'age': 30}",
        "print(my_dict)"
    ],
    "define_set_variable": [
        "# Rearrange the following code blocks to define a set variable and print it:",
        "my_set = {1, 2, 3, 4, 5}",
        "print(my_set)"
    ],
    "define_none_variable": [
        "# Rearrange the following code blocks to define a None variable and print it:",
        "my_none = None",
        "print(my_none)"
    ],
    "convert_variable_type": [
        "# Rearrange the following code blocks to convert a variable to a different data type:",
        "num_str = '42'",
        "num_int = int(num_str)",
        "print(num_int)"
    ]
}




    else:
        puzzles = {
        "list_comprehension": [
            "# Generate squares of numbers 0 through 9",
            "squares = [x**2 for x in range(10)]",
            "print(squares)",
        ],
        "dictionary_comprehension": [
            "# Create a dictionary where the keys are numbers and the values are their squares",
            "squares_dict = {x: x**2 for x in range(5)}",
            "print(squares_dict)",
        ],
        "set_comprehension": [
            "# Generate a set of even numbers from 0 through 9",
            "evens = {x for x in range(10) if x % 2 == 0}",
            "print(evens)",
        ],
        "generator_expression": [
            "# Create a generator for even numbers",
            "even_gen = (x for x in range(10) if x % 2 == 0)",
            "for num in even_gen:",
            "    print(num)",
        ],
        "lambda_function": [
            "# A simple lambda function to add two numbers",
            "add = lambda x, y: x + y",
            "print(add(5, 3))",
        ],
        "map_usage": [
            "# Use map to convert strings to uppercase",
            "words = ['hello', 'world']",
            "upper_words = map(lambda x: x.upper(), words)",
            "print(list(upper_words))",
        ],
        "filter_usage": [
            "# Filter even numbers from a list",
            "numbers = range(10)",
            "even_numbers = filter(lambda x: x % 2 == 0, numbers)",
            "print(list(even_numbers))",
        ],
        "list_slice": [
            "# Reverse a list using slicing",
            "my_list = [1, 2, 3, 4, 5]",
            "reversed_list = my_list[::-1]",
            "print(reversed_list)",
        ],
        }


    # Select one random list from the puzzles
    random_key = random.choice(list(puzzles.keys()))
    code_snippets = puzzles[random_key]

    # Generate a list of indices and shuffle it
    indices = list(range(len(code_snippets)))
    random.shuffle(indices)

    # Pair each shuffled index with its snippet
    shuffled_snippets_with_indices = [
        (index, code_snippets[index]) for index in indices
    ]
    


    progress_percentage = ((user_profile.score % 10) / 10) * 100
    print("pppppppppppppppp", progress_percentage)
    return render(
        request,
        "game.html",
        {
            "snippets_with_indices": shuffled_snippets_with_indices,
            "hint": random_key,
            "score": user_profile.score,
            "badge_level": user_profile.badge_level,
            "progress_percentage": progress_percentage,
            "topic": topic_name,
        },
    )
