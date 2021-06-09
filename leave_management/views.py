import calendar
import datetime
from datetime import timedelta

from django.contrib import messages
from django.http import (HttpRequest, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import render
from django.urls import resolve
from django.views import View

from accounts.models import User
from leave_management.models import Leave

# Create your views here.



def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


class ViewLeaves(View):
    def get(self, request, view_request=None):
        if "view-requests" in resolve(request.path).route:
            users = User.objects.filter(manager=self.request.user)
            requests = Leave.objects.filter(employee__in=users)
            data = {
                "tab": "requests",
                "requests": requests,
            }
            return render(self.request, "leaves.html", {"data": data})
        else:
            leaves = Leave.objects.filter(employee=self.request.user).order_by(
                "-applying_on"
            )
            is_rm = User.objects.filter(manager=self.request.user).exists()
            leaves_taken = sum([leave.in_days for leave in leaves])
            try:
                remaining_leaves = (
                    User.objects.get(email=self.request.user).total_leaves
                    - leaves_taken
                )
            except:
                remaining_leaves = 0
            data = {
                "tab": "leaves",
                "leaves": leaves,
                "is_rm": is_rm,
                "remaining_leaves": remaining_leaves,
            }
            return render(self.request, "leaves.html", {"data": data})

    def post(self, request):
        from_date = datetime.datetime.strptime(request.POST["from_date"], "%Y-%m-%d")
        to_date = datetime.datetime.strptime(request.POST["to_date"], "%Y-%m-%d")
        leaves = Leave.objects.filter(employee=self.request.user).values(
            "from_date", "to_date"
        )
        for leave in leaves:
            if (
                from_date.date() <= leave["to_date"]
                and from_date.date() >= leave["from_date"]
            ):
                messages.error(request, "Leave already applied for some dates.")
                return HttpResponseRedirect("/leave-management/")
            elif (
                to_date.date() <= leave["to_date"]
                and to_date.date() >= leave["from_date"]
            ):
                messages.error(request, "Leave already applied for some dates.")
                return HttpResponseRedirect("/leave-management/")
        reason = request.POST["reason"]
        leave_type = request.POST["leave_type"]
        half_day = False
        if "half_day" in request.POST:
            half_day = True
        un_count_leaves = 0
        total_leaves = (to_date - from_date).days
        for i in range(total_leaves):
            day = calendar.day_name[
                (from_date + datetime.timedelta(days=i + 1)).weekday()
            ]
            un_count_leaves = (
                un_count_leaves + 1
                if day in ["Saturday", "Sunday"]
                else un_count_leaves + 0
            )
        in_days = (total_leaves + 1) - un_count_leaves
        if half_day:
            in_days /= 2
        create_leave = Leave(
            employee=self.request.user,
            is_half_day=half_day,
            from_date=from_date,
            to_date=to_date,
            leave_type=leave_type,
            reason=reason,
            in_days=in_days,
        )
        create_leave.save()
        messages.success(request, "Leave Applied successfully.")
        return HttpResponseRedirect("/leave-management/")


class ChangeRequestApproval(View):
    def post(self, request):
        state = request.POST["approval"]
        leave = Leave.objects.get(id=request.POST["request_id"])
        leave.approval = state
        leave.save()
        # messages.success(request, "Approval status changed.")
        data = {
            "message": "Approval status changed.",
        }
        return JsonResponse(data)
