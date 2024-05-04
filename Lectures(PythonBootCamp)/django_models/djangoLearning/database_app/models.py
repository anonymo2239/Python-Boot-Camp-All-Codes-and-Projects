from django.db import models

# binary field görsel eklemeye yarar.(SQL'de)

class Musician(models.Model):
    name = models.CharField(max_length=50) # çok uzun stringler için textfield kullanılır.
    # gerekli olan fieldları dökümandan okuyabilirsin.
    instrument = models.CharField(max_length=30)
    age = models.IntegerField()
    # ilk önce makemigration'u çalıştırıp programı hazırlamalıyız. Sonra migrate'yi çalıştırmalıyız.
