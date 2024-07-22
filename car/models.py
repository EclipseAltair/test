from django.db import models


class Brand(models.Model):
    class CarType:
        SEDAN = "sedan"
        HATCHBACK = "hatchback"
        PICKUP_TRACK = "pickup_truck"
        SUV = "suv"
        CARGO = "cargo"
        BUS = "bus"

    CAR_TYPE = (
        (CarType.SEDAN, "Седан"),
        (CarType.HATCHBACK, "Хэтчбэк"),
        (CarType.PICKUP_TRACK, "Пикап"),
        (CarType.SUV, "Внедорожник"),
        (CarType.CARGO, "Грузовик"),
        (CarType.BUS, "Автобус"),
    )

    name = models.CharField('Марка', max_length=32)
    model = models.CharField('Модель', max_length=32)
    type = models.CharField('Тип кузова', choices=CAR_TYPE, max_length=32)
    tank_capacity = models.FloatField('Объем бака')
    weight = models.IntegerField('Масса')
    number_of_seats = models.IntegerField('Количество мест')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'Бренды'


class Vehicle(models.Model):
    number = models.CharField('Номер', max_length=16)
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.CASCADE)
    price = models.IntegerField('Стоимость')
    year_of_manufacture = models.CharField('Год выпуска', max_length=4)
    mileage = models.IntegerField('Пробег')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'Автомобили'
