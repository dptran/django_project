from django.db import models

class Inquiry(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email_address = models.EmailField(max_length=100, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Contact: {self.email_address}"