from django.db import models
from django.db.models.base import Model

from accounts.models import User

# Create your models here.


class Leave(models.Model):
    APPROVAL_CHOICES = (
        ("pending", "pending"),
        ("approved", "approved"),
        ("denied", "denied"),
    )
    LEAVE_CHOICES = (
        ("compensatory", "compensatory"),
        ("leave", "leave"),
        ("LOP", "LOP"),
    )
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    reason = models.CharField(max_length=250, blank=True)
    is_half_day = models.BooleanField(default=False)
    applying_on = models.DateTimeField(auto_now=True)
    from_date = models.DateField()
    to_date = models.DateField()
    approval = models.CharField(
        max_length=20, choices=APPROVAL_CHOICES, default="pending"
    )
    leave_type = models.CharField(
        max_length=20, choices=LEAVE_CHOICES, default="compensatory"
    )
    in_days = models.DecimalField(decimal_places=1, max_digits=3, default=0)

    def __str__(self):
        return f"{self.employee.email}"
