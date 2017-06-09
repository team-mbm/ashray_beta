from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustUser(models.Model):
    type_choices = (
        ('SU', 'Super User'),
        ('CC', 'Category Coordinator'),
        ('SC', 'State Coordinator'),
        ('V', 'Volunteer'),
        ('N', 'Normal'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,
                                 default='C')

    user = models.ForeignKey(User)