from django.db import models

# Create your models here.

class courses(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=500)
    courseSummary = models.CharField(max_length=500)
    courseImage = models.CharField(max_length=500)
    courseDate = models.DateField()