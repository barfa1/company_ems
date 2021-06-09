from django.urls import path

from leave_management.views import ChangeRequestApproval, ViewLeaves

app_name = "leave_management"

urlpatterns = [
    path("", ViewLeaves.as_view(), name="view-leaves"),
    path("view-requests/", ViewLeaves.as_view(), name="view-requests"),
    path(
        "change-request-approval/",
        ChangeRequestApproval.as_view(),
        name="change-request-approval",
    ),
]
