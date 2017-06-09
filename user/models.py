from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CustUser(models.Model):
    type_choices = (
        ('SU', 'Super User'),
        ('CC', 'Category Coordinator'),
        ('SC', 'State Coordinator'),
        ('VO', 'Volunteer'),
        ('NO', 'Normal'),
    )
    user_type = models.CharField(max_length=2,
                                 choices=type_choices,)
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.user.username)+" " +str(self.user_type)