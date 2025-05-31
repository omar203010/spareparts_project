from django.db import models

class CarPart(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='car_parts/')

    def __str__(self):
        return self.name
