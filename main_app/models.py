from django.db import models
from django.urls import reverse

CATEGORIES = (
    ('R', 'Rice'),
    ('N', 'Noodles'),
    ('S', 'Soup'),
    ('C', 'Chicken'),
    ('x', 'Side')
)


class Menu(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    note = models.CharField(max_length=256)

    def __str__(self):
        return self.name


