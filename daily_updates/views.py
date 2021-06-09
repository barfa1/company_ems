import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic

from .models import DailyUpdate, Project, User

# Create your views here.


class CreateDailyUpdate(LoginRequiredMixin, generic.CreateView):

    model = DailyUpdate
    fields = "__all__"
    success_url = "/daily-updates/"


class DailyUpdatesView(LoginRequiredMixin, generic.ListView):

    model = DailyUpdate
    template_name = "daily_updates/daily_update.html"
    context_object_name = "daily_updates"  # Default: object_list
    paginate_by = 30

    def get_queryset(self):

        if self.request.GET:
            project = self.request.GET.get("project")
            from_date = self.request.GET.get("from_date")
            to_date = self.request.GET.get("to_date")

            if not project and not from_date and not to_date:
                queryset = (
                    DailyUpdate.objects.filter(
                        date__gte=datetime.date.today() - datetime.timedelta(days=7)
                    )
                    .filter(user=self.request.user)
                    .order_by("-date")
                )

            elif project == "" and from_date and to_date:
                queryset = (
                    DailyUpdate.objects.filter(
                        date__gte=from_date,
                        date__lte=to_date,
                    )
                    .filter(user=self.request.user)
                    .order_by("-date")
                )

            elif project and not from_date and not to_date:
                queryset = (
                    DailyUpdate.objects.filter(project=project)
                    .filter(user=self.request.user)
                    .order_by("-date")
                )

            else:
                queryset = (
                    DailyUpdate.objects.filter(
                        date__gte=from_date,
                        date__lte=to_date,
                        project=project,
                    )
                    .filter(user=self.request.user)
                    .order_by("-date")
                )
        else:
            queryset = (
                DailyUpdate.objects.filter(
                    date__gte=datetime.date.today() - datetime.timedelta(days=7)
                )
                .filter(user=self.request.user)
                .order_by("-date")
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.filter(user=self.request.user)
        context["projects"] = projects
        return context
