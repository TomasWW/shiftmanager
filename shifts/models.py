from django.db import models

# Create your models here.


class Shift(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night'),
        ('off', 'Off'),
    ]

    date = models.DateField()
    shift_type = models.CharField(max_length=10, choices=SHIFT_CHOICES)
    employee = models.ForeignKey("employee.Employee", on_delete=models.CASCADE)

    def is_weekend(self):
        return self.date.weekday() in [5, 6]

    def __str__(self):
        return f"{self.date}. {self.shift_type} ({self.employee})"


class ShiftRequirement(models.Model):
    date = models.DateField
    morning_requirement = models.PositiveIntegerField(default=5)
    evening_requirement = models.PositiveIntegerField(default=5)
    night_requirement = models.PositiveIntegerField(default=2)

    def __str__(self):
        return f"Requirements for {self.date}"
