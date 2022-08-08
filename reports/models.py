from django.db import models

# Create your models here.


class Report(models.Model):
    crime_id = models.BigIntegerField()
    crime_type_name = models.CharField(max_length=255)
    report_date = models.DateTimeField(db_index=True)
    call_date = models.DateTimeField()
    offense_date = models.DateTimeField()
    call_time = models.CharField(max_length=5)
    call_datetime = models.DateTimeField()
    disposition = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    agency_id = models.IntegerField()
    address_type = models.CharField(max_length=255)
    common_location = models.CharField(max_length=255)
