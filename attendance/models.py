from django.db import models

# Create your models here.
from accounts.models import User


class Attendance(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
