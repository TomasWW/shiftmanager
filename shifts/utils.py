import calendar
from datetime import date
from .models import Shift


def genereate_month(year, month):
    cal = calendar.Calendar()
    days = []
    for day in cal.itermonthdates(year, month):
        days.append({
            "date": day,
            "weekday": day.weekday(),
            "is_weekend": day.weekday() in (5, 6),
            "shifts": Shift.objects.filter(date=day)
        })
    return days
