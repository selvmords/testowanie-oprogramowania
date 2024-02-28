from django.db import models

# Create your models here.

class ListCars(models.Model):
    nameCar = models.CharField(max_length=255)
    content = models.TextField(db_default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=2000)
    imgCar = models.ImageField(upload_to="mediacar", blank=True, null=True)

    def __str__(self):
        return self.nameCar