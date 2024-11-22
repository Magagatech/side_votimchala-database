from django.db import models

class Post(models.Model):
    user = models.CharField(max_length=100)
    handle = models.CharField(max_length=100)
    profile_image = models.URLField()
    image = models.URLField()
    text = models.TextField()
    hashtags = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: {self.text[:30]}"
