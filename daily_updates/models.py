from django.db import models

# Create your models here.
from accounts.models import User
from projects.models import Project


class DailyUpdate(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billable = models.IntegerField(default=0)
    description_bh = models.TextField()
    non_billable = models.IntegerField(default=0)
    description_nbh = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.date)
