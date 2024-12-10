from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=48)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'db_books'