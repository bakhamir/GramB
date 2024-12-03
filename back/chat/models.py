from django.db import models
from django.utils.timezone import now

class Message(models.Model):
    username = models.CharField(max_length=50, default="anon#000000")
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.username}: {self.content[:30]}"
