from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import Holiday

# Create your views here.


class HolidayView(LoginRequiredMixin, generic.ListView):
    model = Holiday
    template_name = "holiday/holiday.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["holidays"] = Holiday.objects.filter(type="holiday")
        context["optionals"] = Holiday.objects.filter(type="optional")
        return context
