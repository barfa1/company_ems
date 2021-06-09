from django.db import models

# Create your models here.


class Holiday(models.Model):
    optional = "optional"
    holiday = "holiday"

    holiday_type = (
        ("", "Please select holiday type"),
        (optional, "Optional"),
        (holiday, "Holiday"),
    )
    name = models.CharField(max_length=256)
    date = models.DateField()
    description = models.TextField(blank=True)
    type = models.CharField(choices=holiday_type, max_length=256)

    def __str__(self):
        return self.name
