from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="goals"
    )
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

