from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # If a user is deleted, all Task data is deleted
    title = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True
    )  # Gives us a text box and a little more options
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["complete"]
