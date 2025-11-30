from django.shortcuts import render
from .utils import generate_month


def calendar_view(request):
    days = generate_month()
    return render(request, "shifts/calendar.html", {"days": days})
