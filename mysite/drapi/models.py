from django.db import models

# Create your models here.
class Aiquest(models.Model):
    teachers_name = models.CharField(max_length=25)
    course_name = models.CharField(max_length=25)
    course_duration = models.IntegerField()
    sit = models.IntegerField()
