from django.db import models

# Create your models here.
class Car(models.Model):
    make_model_year = models.CharField(max_length=128)
    license_plate = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    route = models.CharField(max_length=128)

    def __str__(self):
        return self.license_plate

class Driver(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dob = models.IntegerField()
    permit_number = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    contact_number = models.CharField(max_length=128)
    # car = models.ForeignKey(Car,related_name='cars',on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
