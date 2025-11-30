import calendar
from datetime import date
from .models import Shift


def generate_month(year=None, month=None):
    today = date.today()
    if year is None:
        year = today.year
    if month is None:
        month = today.month

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
