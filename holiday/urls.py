from django.urls import path

from holiday.views import HolidayView

app_name = "holiday"

urlpatterns = [
    path("", HolidayView.as_view(), name="holiday"),
]
