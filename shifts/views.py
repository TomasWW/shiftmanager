from django.shortcuts import render


from django.shortcuts import render
from .utils import generate_month


def calendar_view(request, year, month):
    days = generate_month(year, month)
    return render(request, "shifts/calendar.html", {"days": days})
