from django.urls import path

from . import views

app_name = "attendance"

urlpatterns = [
    path("", views.AttendanceView.as_view(), name="attendance"),
]
