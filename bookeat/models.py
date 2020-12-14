from django.db import models
from django.utils import timezone

class User(models.Model):
    real_name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.real_name

class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.IntegerField(max_length=5)
    size_table = models.IntegerField(max_length=5)
    def __int__(self):
        return self.table_id

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateTimeField('Booking date')
    def __str__(self):
        return self.booking_date
    def was_booked_recently(self):
        return self.booking_date >= timezone.now() - datetime.timedelta(days=1)