from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="static/files")
class sales(models.Model):
    invoice_id = models.CharField(max_length=15)
    product_line = models.CharField(max_length=20)
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    tax = models.FloatField()
    total = models.FloatField()
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.invoice_id
