from django.db import models


# Create your models here.
class CouseModel(models.Model):
    coursename = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.coursename
