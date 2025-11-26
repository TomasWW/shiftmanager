from django.db import models

class Employee(models.Model):
    GROUP_CHOICES = [
        ('green','Green'),
        ('blue', 'Blue')
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    work_percentage = models.PositiveIntegerField(default=100)
    group = models.CharField(max_length=10, choices=GROUP_CHOICES)
    cycle_index = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name}, ({self.group})"
    
    