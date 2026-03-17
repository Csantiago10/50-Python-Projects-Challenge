from django.db import models

# Create your models here.
class Computer(models.Model):
    brand = models.CharField(max_length=100)
    motherboard = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    monitor = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    mouse = models.CharField(max_length=100)
    

    def __str__(self):
        return self.brand + ' ' + self.motherboard + ' ' + self.processor + ' ' + self.ram + ' ' + self.storage + ' ' + self.monitor + ' ' + self.keyboard + ' ' + self.mouse