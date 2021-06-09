from django.urls import path

from . import views

app_name = "daily_updates"

urlpatterns = [
    path("", views.DailyUpdatesView.as_view(), name="daily-update"),
    path("create-update/", views.CreateDailyUpdate.as_view(), name="create-update"),
]
