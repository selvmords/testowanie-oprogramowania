from django.db import models


# Create your models here.
class CarList(models.Model):
    nameCar = models.CharField(max_length=255)
    content = models.TextField(default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=1000)
    imgCar = models.ImageField(upload_to='mediaCar', blank=True, null=True)

    def __str__(self):
        return self.nameCar

