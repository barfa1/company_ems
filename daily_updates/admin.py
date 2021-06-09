from django.contrib import admin

# Register your models here.
from .models import DailyUpdate


class DailyUpdateAdmin(admin.ModelAdmin):
    pass


admin.site.register(DailyUpdate, DailyUpdateAdmin)
