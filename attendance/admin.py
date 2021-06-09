from django.contrib import admin

# Register your models here.
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Attendance, AttendanceAdmin)
