from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Attendance

# Create your views here.


class AttendanceView(LoginRequiredMixin, generic.ListView):
    model = Attendance
    template_name = "attendance/attendance.html"
