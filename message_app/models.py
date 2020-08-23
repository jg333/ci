from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Message(models.Model):
    CHOICES = [
        ("question", "Pytanie"),
        ("other", "Inne")
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    priority = models.IntegerField()
    category = models.CharField(max_length=10, choices=CHOICES)
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.subject} from {self.email}"

    def get_absolute_url(self):
        return reverse('message_app:message_list')

    def is_valid_message(self):
        return self.priority > 0 and self.priority <= 10

    def increase_priority(self):
        self.priority += 1
