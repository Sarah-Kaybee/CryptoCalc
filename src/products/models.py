from django.db import models

# === WHEN UPDATING MODELS, always run:
# # # > python manage.py makemigrations
# # # > python manage.py migrate


# Create your models here.
class Product(models.Model):
    title =       models.CharField(max_length=120)    # max_length: required
    description = models.TextField(blank=True, null=True)
    price =       models.DecimalField(max_digits=15, decimal_places=2)
    summary =     models.TextField(blank=True, null=False)
    featured =    models.BooleanField(default=True)

# blank=True means it is non-essential to fill out the box.
# null=True means NULL fields are allowed. Don't use for a primary key lol.
