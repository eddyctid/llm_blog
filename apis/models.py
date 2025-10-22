from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # get reference to the user model

class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    post_title = models.CharField(max_length=255)
    post_body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
