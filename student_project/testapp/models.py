from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class STUDENT(models.Model):
    STUDENT_NAME = models.CharField(max_length=30)
    STUDENT_MARKS = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    STUDENT_DOB = models.DateField(null='True')
    STUDENT_DOJ = models.DateField(null='True')