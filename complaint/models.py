from django.db import models
from user.models import CustUser
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Complaint(models.Model):

    status_choice=(
        ("URV", "Under Review Of Volunteer"),
        ("URSC","Under Review Of State Coordinator"),
        ("URCC","Under Review Of Category Coordinator"),
        ("URA","Under Review Of Admin"),
        ("AP", "Approved"),
        ("RJ", "Rejected"),
    )

    status = models.CharField(max_length=5, choices=status_choice,default="UR")
    category = models.ForeignKey(Category, blank=True, null=True)
    complaint_user = models.ForeignKey(CustUser, blank=True, null=True)
    location = models.CharField(max_length=100)
    name_child = models.CharField(max_length=25, blank=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return str(self.name_child)+" "+str(self.category)

## class PreviousWork(models.Model):

