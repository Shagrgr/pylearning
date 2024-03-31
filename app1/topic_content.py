class TopicContent:
    def __init__(self, name):
        self.name = name
        self.content = self.get_content()

    def get_content(self):
        if self.name == "Inheritance":
            return {
    'full': '''
        <div class="content">
            <h2>Very Detailed Note on Python Inheritance:</h2>
            <p>Introduction: Inheritance is a core concept in object-oriented programming (OOP) that enables the creation of new classes based on existing ones. In Python, it allows a class (subclass) to inherit attributes and methods from another class (superclass). This note will delve deeply into the mechanics, applications, and intricacies of Python inheritance.</p>
            <h3>Mechanics of Inheritance:</h3>
            <ul>
                <li><strong>Syntax:</strong> In Python, inheritance is achieved by specifying the superclass(es) inside parentheses after the subclass name. For example:<br><code>class Subclass(Superclass):</code></li>
                <li><strong>Super() Function:</strong> Used to call methods and constructors of the superclass within the subclass. For example:<br><code>super().__init__()</code></li>
                <li><strong>Method Resolution Order (MRO):</strong> Determines the order in which Python searches for methods in a hierarchy of classes. For example:<br><code>ClassName.__mro__</code></li>
            </ul>
            <h3>Types of Inheritance:</h3>
            <ul>
                <li><strong>Single Inheritance:</strong> Subclass inherits from only one superclass.</li>
                <li><strong>Multiple Inheritance:</strong> Subclass inherits from multiple superclasses.</li>
                <li><strong>Multilevel Inheritance:</strong> Involves a chain of inheritance where a subclass inherits from another subclass.</li>
            </ul>
            <h3>Advanced Concepts:</h3>
            <ul>
                <li><strong>Overriding Methods:</strong> Subclasses can provide a specific implementation of a method defined in the superclass.</li>
                <li><strong>Abstract Base Classes (ABCs):</strong> Used to define abstract methods that must be implemented by subclasses.</li>
                <li><strong>Mixin Classes:</strong> Provide additional functionality to classes through multiple inheritance.</li>
            </ul>
            <h3>Benefits and Best Practices:</h3>
            <ul>
                <li><strong>Code Reusability:</strong> Avoids redundancy by inheriting attributes and methods.</li>
                <li><strong>Polymorphism:</strong> Enables objects to be treated as instances of their superclass, promoting flexibility.</li>
                <li><strong>Readability and Maintenance:</strong> Enhances code organisation and clarity by establishing hierarchical relationships.</li>
            </ul>
            <h3>Considerations and Caveats:</h3>
            <ul>
                <li><strong>Avoid Deep Inheritance Hierarchies:</strong> Excessive nesting can lead to complex code and maintenance challenges.</li>
                <li><strong>Diamond Problem:</strong> Arises in multiple inheritance when a method is overridden by more than one superclass.</li>
                <li><strong>Composition over Inheritance:</strong> Sometimes, composition might be preferred over inheritance to avoid tight coupling.</li>
            </ul>
            <h3>Applications and Examples:</h3>
            <ul>
                <li><strong>Software Design:</strong> Inheritance facilitates modular design, allowing for the creation of reusable components.</li>
                <li><strong>Framework Development:</strong> Frameworks often leverage inheritance to provide extensibility and customization.</li>
                <li><strong>GUI Development:</strong> Inheritance is used to create custom widgets and components in graphical user interfaces.</li>
            </ul>
            <h3>Conclusion:</h3>
            <p>Python inheritance is a foundational concept in OOP, offering powerful mechanisms for code reuse, extensibility, and maintainability. Understanding its mechanics and applying best practices can greatly enhance the design and scalability of Python applications.</p>
        </div>
    ''',
    'brief': '''
        <div class="content">
            <h2>Intermediate Note on Python Inheritance:</h2>
            <p>Introduction: Inheritance in Python is a key concept in object-oriented programming that allows for the creation of new classes based on existing ones. This note provides an intermediate-level overview of Python inheritance, covering its syntax, types, applications, and best practices.</p>
            <h3>Syntax and Mechanics:</h3>
            <ul>
                <li><strong>Inheritance:</strong> Inheritance is declared by specifying the superclass(es) inside parentheses after the subclass name. For example:<br><code>class Subclass(Superclass):</code></li>
                <li><strong>Super() Function:</strong> Used to access methods and attributes from the superclass within the subclass. For example:<br><code>super().__init__()</code></li>
                <li><strong>Method Resolution Order (MRO):</strong> Determines the order in which Python searches for methods in a class hierarchy. For example:<br><code>ClassName.__mro__</code></li>
            </ul>
            <h3>Types of Inheritance:</h3>
            <ul>
                <li><strong>Single Inheritance:</strong> Subclass inherits from only one superclass.</li>
                <li><strong>Multiple Inheritance:</strong> Subclass inherits from multiple superclasses.</li>
                <li><strong>Multilevel Inheritance:</strong> Involves a chain of inheritance where a subclass inherits from another subclass.</li>
            </ul>
            <h3>Advanced Concepts:</h3>
            <ul>
                <li><strong>Method Overriding:</strong> Subclasses can override methods defined in the superclass with their own implementation.</li>
                <li><strong>Abstract Base Classes (ABCs):</strong> Define abstract methods that must be implemented by subclasses.</li>
                <li><strong>Mixin Classes:</strong> Provide additional functionality to classes through multiple inheritance.</li>
            </ul>
            <h3>Benefits and Best Practices:</h3>
            <ul>
                <li><strong>Code Reusability:</strong> Inheritance promotes reuse of code and reduces redundancy.</li>
                <li><strong>Polymorphism:</strong> Allows objects to be treated as instances of their superclass, enabling flexibility.</li>
                <li><strong>Readability and Maintenance:</strong> Enhances code organization and clarity by establishing hierarchical relationships.</li>
            </ul>
            <h3>Considerations and Caveats:</h3>
            <ul>
                <li><strong>Deep Inheritance Hierarchies:</strong> Avoid excessive nesting to prevent complexity and maintainability issues.</li>
                <li><strong>Diamond Problem:</strong> Occurs in multiple inheritance when a method is overridden by more than one superclass.</li>
                <li><strong>Composition over Inheritance:</strong> Sometimes, composition may be preferred over inheritance for better flexibility.</li>
            </ul>
            <h3>Applications and Examples:</h3>
            <ul>
                <li><strong>Software Design:</strong> Inheritance facilitates modular design and the creation of reusable components. For example:<br><code>class Animal:</code><br><code>class Dog(Animal):</code></li>
                <li><strong>Framework Development:</strong> Frameworks leverage inheritance for extensibility and customization.</li>
                <li><strong>GUI Development:</strong> Inheritance is used to create custom widgets and components in graphical user interfaces.</li>
            </ul>
            <h3>Conclusion:</h3>
            <p>Python inheritance is a powerful mechanism in object-oriented programming, enabling code reuse, extensibility, and maintainability. By understanding its syntax, types, and best practices, developers can design more scalable and maintainable Python applications.</p>
        </div>
    ''',
    'summary': '''
        <div class="content">
            <h2>Summary Note on Python Inheritance:</h2>
            <p>Introduction: Inheritance is a fundamental concept in Python's object-oriented programming paradigm, allowing classes to inherit attributes and methods from other classes. This summary note provides a concise overview of Python inheritance, highlighting its syntax, types, benefits, and considerations.</p>
            <h3>Key Points</h3>
            <ul>
                <li><strong>Syntax:</strong> Inheritance is declared by specifying superclass(es) inside parentheses after the subclass name.</li>
                <li><strong>Types of Inheritance:</strong> Python supports single, multiple, and multilevel inheritance, facilitating diverse class hierarchies.</li>
                <li><strong>Benefits:</strong> Python inheritance promotes code reusability, polymorphism, and readability, enhancing software design and development.</li>
                <li><strong>Considerations:</strong> Developers should be mindful of deep inheritance hierarchies and the diamond problem, opting for composition over inheritance when necessary.</li>
            </ul>
            <h3>Conclusion</h3>
            <p>Python inheritance is a powerful mechanism for enhancing code scalability and maintainability in object-oriented programming. By understanding its syntax, types, benefits, and considerations, developers can design more scalable and maintainable Python applications.</p>
        </div>
    '''
}

        elif self.name == "Arrays":
            return {
    'full': '''
        <div class="content">
            <h2>Very Detailed Note on Python Arrays:</h2>
            <p><strong>Introduction to Python Arrays:</strong> Python arrays represent sequential collections of elements stored in contiguous memory locations. Unlike lists, they are optimized for homogeneous data, enhancing memory efficiency and access speed, especially for large datasets.</p>
            <p><strong>Creating Arrays:</strong> Python arrays are instantiated using the array module, requiring specification of a typecode representing the data type of elements and optionally initialized with specific values.</p>
            <p><strong>Accessing and Manipulating Elements:</strong> Arrays support various operations like insertion, deletion, slicing, concatenation, and iteration, similar to lists, ensuring efficient manipulation and processing of array elements.</p>
            <p><strong>Type Codes and Memory Efficiency:</strong> Type codes dictate the data type of array elements, influencing memory efficiency. Arrays store elements in contiguous memory, resulting in faster access times and reduced memory overhead, ideal for numerical computations and large datasets.</p>
            <p><strong>Limitations and Use Cases:</strong> While arrays excel in memory efficiency and numerical computations, their restriction to homogeneous data makes them unsuitable for heterogeneous datasets. However, they are indispensable for tasks requiring memory optimization and uniform data types.</p>
            <pre><code>import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1

# Insert element
arr.insert(2, 6)  # Inserts 6 at index 2

# Delete element
arr.remove(3)  # Removes the first occurrence of 3

# Concatenate arrays
arr2 = array.array('i', [7, 8, 9])
arr += arr2

# Print array
print(arr)  # Output: array('i', [1, 2, 6, 4, 5, 7, 8, 9])</code></pre>
            <p><strong>Conclusion:</strong> Python arrays offer a memory-efficient solution for storing homogeneous data collections. Despite limitations regarding heterogeneous data, they are invaluable for numerical computations and memory-sensitive applications. Proficiency in array manipulation is essential for efficient Python programming.</p>
        </div>
    ''',
    'brief': '''
        <div class="content">
            <h2>Intermediate Note on Python Arrays:</h2>
            <p><strong>Introduction to Python Arrays:</strong> Python arrays provide a specialized means to store homogeneous data efficiently. Optimized for numerical computations and large datasets, arrays offer memory-efficient storage compared to lists.</p>
            <p><strong>Creating and Accessing Arrays:</strong> Arrays are instantiated using the array module, specifying a typecode for element data type. Accessing array elements is similar to lists, allowing for efficient data retrieval and manipulation.</p>
            <p><strong>Common Operations:</strong> Arrays support operations like insertion, deletion, slicing, concatenation, and iteration, enabling efficient data processing and analysis, particularly in scientific computing and numerical tasks.</p>
            <p><strong>Type Codes and Memory Efficiency:</strong> Type codes define the data type of array elements, influencing memory usage. Arrays store data in contiguous memory, resulting in faster access times and reduced memory overhead.</p>
            <p><strong>Limitations and Use Cases:</strong> While arrays excel in memory efficiency and numerical tasks, they are restricted to homogeneous data, limiting their applicability for heterogeneous datasets. Nonetheless, they are indispensable for memory-sensitive applications.</p>
            <pre><code>import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1

# Insert element
arr.insert(2, 6)  # Inserts 6 at index 2

# Delete element
arr.remove(3)  # Removes the first occurrence of 3

# Concatenate arrays
arr2 = array.array('i', [7, 8, 9])
arr += arr2

# Print array
print(arr)  # Output: array('i', [1, 2, 6, 4, 5, 7, 8, 9])</code></pre>
            <p><strong>Conclusion:</strong> Python arrays serve as efficient data structures for storing homogeneous collections. Their role in numerical computations and memory optimization makes them indispensable for various scientific and computational tasks.</p>
        </div>
    ''',
    'summary': '''
        <div class="content">
            <h2>Summary Note on Python Arrays:</h2>
            <p><strong>Introduction to Python Arrays:</strong> Python arrays are specialized data structures tailored for efficient storage of homogeneous collections. Unlike lists, arrays optimize memory usage and access speed by restricting data types to homogeneity.</p>
            <p><strong>Creating and Accessing Arrays:</strong> Arrays are instantiated using the array module, with a typecode specifying the element data type. Accessing array elements mirrors list indexing, ensuring familiar and efficient data manipulation.</p>
            <p><strong>Common Operations:</strong> Arrays support operations like insertion, deletion, slicing, concatenation, and iteration, facilitating efficient data processing and analysis, particularly in scientific computing and numerical tasks.</p>
            <p><strong>Type Codes and Memory Efficiency:</strong> Type codes define the data type of array elements, influencing memory usage. Arrays store data in contiguous memory, leading to faster access times and reduced memory overhead.</p>
            <p><strong>Limitations and Use Cases:</strong> While arrays excel in memory efficiency and numerical tasks, they are restricted to homogeneous data, limiting their applicability for heterogeneous datasets. Nonetheless, they are indispensable for memory-sensitive applications.</p>
            <pre><code>import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Access elements
print(arr[0])  # Output: 1

# Insert element
arr.insert(2, 6)  # Inserts 6 at index 2

# Delete element
arr.remove(3)  # Removes the first occurrence of 3

# Concatenate arrays
arr2 = array.array('i', [7, 8, 9])
arr += arr2

# Print array
print(arr)  # Output: array('i', [1, 2, 6, 4, 5, 7, 8, 9])</code></pre>
            <p><strong>Conclusion:</strong> Python arrays offer a specialized and memory-efficient solution for storing homogeneous data collections. Their importance in numerical computations and memory-sensitive applications cannot be overstated, making proficiency in array manipulation essential for efficient Python programming.</p>
        </div>
    '''
}


        elif self.name == "Control Structures":
            return {
    'full': '''
        <div class="content">
            <h2>Exploring Python Control Structures</h2>
            <p>Python, a dynamic and intuitive programming language, offers a suite of control structures enabling developers to dictate the flow of their code's execution. These structures include conditionals and loops, which are pivotal for creating efficient and effective scripts.</p>
            <p>This guide delves into the core control structures in Python, namely:</p>
            <ul>
                <li><strong>If Statement:</strong> Facilitates conditional execution based on the evaluation of a condition. Incorporates "else" and "elif" for comprehensive flow control.</li>
                <li><strong>While Loop:</strong> Enables the execution of a code block while a specified condition remains true, with a cautionary note on avoiding infinite loops.</li>
                <li><strong>For Loop:</strong> Iterates over sequences or iterable objects, allowing for clean and concise looping through known data structures.</li>
            </ul>
            <h3>Control Structure Syntax and Examples</h3>
            <p>Below are examples demonstrating the syntax and application of each control structure:</p>
            <pre><code>x = 5
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)</code></pre>
            <p>Understanding and utilizing these control structures efficiently is crucial for Python programming, aiding in the development of logical and readable code.</p>
        </div>
    ''',
    'brief': '''
        <div class="content">
            <h2>Mastering Python Control Structures</h2>
            <p>Python's control structures, such as "if", "else", "while", and "for" loops, are fundamental for directing the execution flow of programs. They are essential for performing conditional operations, repeating tasks, and iterating over data structures.</p>
            <p>Highlighted below is a concise overview and examples of Python control structures:</p>
            <pre><code>temperature = 25
if temperature > 30:
    print("It's hot outside")
elif 20 <= temperature <= 30:
    print("It's a pleasant day")
else:
    print("It's cold outside")

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)</code></pre>
            <p>Proficiency in these constructs enhances a programmer's capability to solve complex problems with elegant and efficient code.</p>
        </div>
    ''',
    'summary': '''
        <div class="content">
            <h2>Python Control Structures: An Overview</h2>
            <p>Python's control structures, including conditional statements and loops, are pivotal for executing code based on conditions, performing repetitive tasks, and iterating over sequences. These structures form the backbone of Python programming, enabling the creation of flexible and dynamic applications.</p>
            <p>The "Hello, World!" example is a simple yet effective demonstration of Python's accessible syntax, serving as a gateway to understanding more complex programming constructs.</p>
            <p>Embracing these control structures is vital for any aspiring Python developer, laying the foundation for mastering the language's vast capabilities across various programming paradigms.</p>
        </div>
    '''
}

       


        elif self.name == "Data Types":
                    return {
    'full': '''
        <div class="content">
            <h2>Very Detailed Note: Python Data Types</h2>
            <p>Python, as a dynamically typed language, offers a wide range of built-in data types to efficiently handle various kinds of data. A comprehensive understanding of these data types is essential for effective programming and data manipulation. Below is an exhaustive examination of Python data types:</p>
            <h3>Numeric Types:</h3>
            <ul>
                <li><strong>int:</strong> Represents integers, positive or negative whole numbers without any decimal point. Example: <code>x = 5</code></li>
                <li><strong>float:</strong> Denotes floating-point numbers, numbers with a decimal point or in exponential form. Example: <code>y = 3.14</code></li>
                <li><strong>complex:</strong> Represents complex numbers in the form a + bj, where a and b are floats and j is the imaginary unit. Example: <code>z = 3 + 4j</code></li>
            </ul>
            <h3>Sequence Types:</h3>
            <ul>
                <li><strong>str:</strong> Denotes strings, which are sequences of characters enclosed within single, double, or triple quotes. Example: <code>text = "Hello, World!"</code></li>
                <li><strong>list:</strong> Represents lists, ordered and mutable collections of items. Example: <code>my_list = [1, 2, 3, 'a', 'b', 'c']</code></li>
                <li><strong>tuple:</strong> Denotes tuples, ordered and immutable collections of items. Example: <code>my_tuple = (1, 2, 3, 'a', 'b', 'c')</code></li>
            </ul>
            <h3>Mapping Type:</h3>
            <ul>
                <li><strong>dict:</strong> Represents dictionaries, unordered collections of key-value pairs. Example: <code>my_dict = {'name': 'John', 'age': 30}</code></li>
            </ul>
            <h3>Set Types:</h3>
            <ul>
                <li><strong>set:</strong> Denotes sets, unordered collections of unique items. Example: <code>my_set = {1, 2, 3, 4, 5}</code></li>
                <li><strong>frozenset:</strong> Represents immutable sets, similar to sets but immutable once defined. Example: <code>my_frozenset = frozenset({1, 2, 3, 4, 5})</code></li>
            </ul>
            <h3>Boolean Type:</h3>
            <ul>
                <li><strong>bool:</strong> Represents Boolean values True or False. Example: <code>is_valid = True</code></li>
            </ul>
            <h3>None Type:</h3>
            <ul>
                <li><strong>None:</strong> Denotes the absence of a value or a null value. Example: <code>x = None</code></li>
            </ul>
            <p>Python data types can be converted from one type to another using built-in functions like <code>int()</code>, <code>float()</code>, <code>str()</code>, etc. The appropriate selection of data types can significantly impact code performance and readability. Python also supports complex data structures like nested lists, dictionaries of dictionaries, lists of tuples, etc., enabling sophisticated data modeling and processing.</p>
        </div>
    ''',
    'brief': '''
        <div class="content">
            <h2>Intermediary Note: Python Data Types</h2>
            <p>Python, as a dynamically typed language, offers various built-in data types suitable for different kinds of data manipulation. Here's a comprehensive overview of Python data types:</p>
            <h3>Numeric Types:</h3>
            <ul>
                <li><strong>int:</strong> Represents integers without any decimal point.</li>
                <li><strong>float:</strong> Represents floating-point numbers with a decimal point or in exponential form.</li>
                <li><strong>complex:</strong> Represents complex numbers with real and imaginary parts.</li>
            </ul>
            <h3>Sequence Types:</h3>
            <ul>
                <li><strong>str:</strong> Represents strings, sequences of characters.</li>
                <li><strong>list:</strong> Represents lists, ordered and mutable collections.</li>
                <li><strong>tuple:</strong> Represents tuples, ordered and immutable collections.</li>
            </ul>
            <h3>Mapping Type:</h3>
            <ul>
                <li><strong>dict:</strong> Represents dictionaries, unordered collections of key-value pairs.</li>
            </ul>
            <h3>Set Types:</h3>
            <ul>
                <li><strong>set:</strong> Represents sets, unordered collections of unique items.</li>
                <li><strong>frozenset:</strong> Represents immutable sets.</li>
            </ul>
            <h3>Boolean Type:</h3>
            <ul>
                <li><strong>bool:</strong> Represents Boolean values True or False.</li>
            </ul>
            <h3>None Type:</h3>
            <ul>
                <li><strong>None:</strong> Represents the absence of a value or a null value.</li>
            </ul>
            <p>Python provides built-in functions for type conversion like <code>int()</code>, <code>float()</code>, <code>str()</code>, etc. Choosing the appropriate data type is crucial for efficient code. Python also supports complex data structures for advanced data modeling.</p>
        </div>
    ''',
    'summary': '''
        <div class="content">
            <h2>Summary Note: Python Data Types</h2>
            <p>Python offers a variety of built-in data types suitable for diverse data manipulation tasks. Here's a quick summary:</p>
            <ul>
                <li><strong>Numeric Types:</strong> int, float, complex</li>
                <li><strong>Sequence Types:</strong> str, list, tuple</li>
                <li><strong>Mapping Type:</strong> dict</li>
                <li><strong>Set Types:</strong> set, frozenset</li>
                <li><strong>Boolean Type:</strong> bool</li>
                <li><strong>None Type:</strong> None</li>
            </ul>
            <p>Understanding and selecting the right data type is crucial for efficient programming. Python also supports type conversion and complex data structures for advanced data modeling.</p>
        </div>
    '''
}



        else:
            return {}