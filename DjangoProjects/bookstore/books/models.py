from django.db import models
"VERİ TABANI İLE ENTEGRSYONU models.py sağlar. tablolar vs."
# Create your models here.

#author(yazar) sınıfı oluşturduk
class Author(models.Model):
    name=models.CharField(max_length=50)
    created =models.DateTimeField('date created')