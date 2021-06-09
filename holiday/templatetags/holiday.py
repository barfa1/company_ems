import datetime
from datetime import date

from django import template

register = template.Library()


def get_day(passed_date):
    # print(str(passed_date))
    year, month, day = str(passed_date).split("-")
    day_name = datetime.date(int(year), int(month), int(day))
    return day_name.strftime("%A")


register.filter("get_day", get_day)
