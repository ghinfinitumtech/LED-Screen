# models.py
from django.db import models

class ParliamentCategory(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)
    def __str__(self):
        return str(self.name)

class AssemblyCategory(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return str(self.name)


class GovtEvent(models.Model):
    name = models.CharField(max_length=100, null=True)
    parliament = models.ForeignKey(ParliamentCategory, on_delete=models.CASCADE)
    assembly = models.ForeignKey(AssemblyCategory, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100, null=True)
    pre_event_image = models.ImageField(upload_to='images')
    mid_event_image = models.ImageField(upload_to='images')
    post_event_image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return str(self.name)
