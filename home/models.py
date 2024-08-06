from django.db import models

# Create your models here.
class Contact(models.Model):
    STATES = [
        ('Punjab', 'Punjab'),
        ('Sindh', 'Sindh'),
        ('KPK', 'KPK'),
        ('Balochistan', 'Balochistan'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATES)
    zip_code = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
