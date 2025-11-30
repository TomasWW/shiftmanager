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
