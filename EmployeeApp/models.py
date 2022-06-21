from django.db import models

class EmpModel(models.Model):
    empName = models.CharField(max_length=30)
    empSal = models.FloatField()
    empAddress = models.CharField(max_length=50)
    empEmail = models.EmailField()
