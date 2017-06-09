from django.db import models

# Create your models here.

class AnganwadiComplaint(models.Model):

    complaint_user = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=100)
    name_child = models.CharField(max_length=25, blank=True)
    desc = models.TextField(blank=True)
    status_choice=(
        ("AP","Approved"),
        ("RJ","Rejected"),
        ("PD","Pending"),
    )
    status = models.CharField(max_length=2, choices=status_choice)

    def __str__(self):
        return str(self.complaint_user) + " " + str(self.name_child)
