from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Menu(models.Model):

    CATEGORIES = (
    ('R', 'Rice'),
    ('N', 'Noodles'),
    ('S', 'Soup'),
    ('C', 'Chicken'),
    ('x', 'Side')
    )

    CATEGORY_ORDER = {
        'C': 1,
        'R': 2,
        'N': 3,
        'S': 4,
        'x': 5
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    note = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse('menu')

    def __str__(self):
        return f"{self.title} id is {self.id}"



class Photo(models.Model):
    url = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='photos')


    def __str__(self):
        return f"Photo for menu_id: {self.menu_id} @{self.url}"