from django.db import models

from accounts.models import User


class Project(models.Model):

    name = models.CharField(max_length=256)
    user = models.ManyToManyField(User, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
