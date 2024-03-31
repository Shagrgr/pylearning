from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    badge_level = models.IntegerField(default=1)
    last_score_update = models.DateTimeField(auto_now=True)  # Automatically updates to the current time

    def __str__(self):
        return f"{self.user.username}'s profile"

    def update_score_and_badge(self, points):
        self.score += points
        score = self.score
        counter = 1
        while score > 10:
            counter += 1
            score /= 10
        self.badge_level = counter
        self.save()  # This will also update 'last_score_update' to the current time
        
    def get_score(self):
        return self.score

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_at}"
    

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    topic = models.CharField(max_length=100)  # Assuming a topic is a simple string
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note on {self.topic} by {self.user.username}"

