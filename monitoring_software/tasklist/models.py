from django.db import models
from accounts.models import User

class Task(models.Model):
    title = models.CharField(max_length = 200)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    description = models.TextField()
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.title