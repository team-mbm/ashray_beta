from django.db import models
from complaint.models import Category
# Create your models here.

class MapperNGO(models.Model):


    category = models.ForeignKey(Category,blank=True, null=True)
    ngo_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.ngo_name