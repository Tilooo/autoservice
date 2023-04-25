from django.db import models

# Create your models here.
class VehicleModel(models.Model):
    make = models.CharField(verbose_name='Gamintojas', max_length=50)
    model = models.CharField(verbose_name='Modelis', max_length=50)


class Service(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=50)
    price = models.IntegerField(verbose_name='Kaina')


class vehicle(models.Model):
    plate = models.CharField(verbose_name='valstybinis numeris', max_length=6)
    vin = models.CharField(verbose_name='VIN kodas', max_length=17)
    owner_name = models.CharField(verbose_name='Savininkas', max_length=50)
    vehicle_model = models.CharField(to='VehicleModel', verbose_name='Automobilio modelis', on_delete=models.SET_NULL, null=True)


class Order(models.Model):
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    vehicle = models.ForeignKey(to='Vehicle', on_delete=models.SET_NULL, null=True)

class OrderLine(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    service = models.ForeignKey(to='Service', verbose_name='Paslauga', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(verbose_name='Kiekis')


