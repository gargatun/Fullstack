from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
