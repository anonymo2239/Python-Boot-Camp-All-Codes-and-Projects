from django.db import models

# binary field görsel eklemeye yarar.(SQL'de)

class Musician(models.Model):
    name = models.CharField(max_length=50) # çok uzun stringler için textfield kullanılır.
    # gerekli olan fieldları dökümandan okuyabilirsin.
    instrument = models.CharField(max_length=30)
    age = models.IntegerField()
    # ilk önce makemigration'u çalıştırıp programı hazırlamalıyız. Sonra migrate'yi çalıştırmalıyız.
    # python manage.py makemigrations database_app
    # python manage.py sqlmigrate database_app 0001

    # MANAGE.PY I KULLANARAK TERMİNALDE BİR SHELL AÇABİLİRİZ (python manage.py shell yazarsak jupyter
    # notebook gibi tek satirli kod yazabiliriz.)

    # models kullanarak databes e veri kaydetme
    # 1) james = Musician(name="James", instrument="Drum", age=60)
    #    james.save() //burada bir satır kaydetmiş olduk(INSERT komutu gibi)

    # 2) Musician.objects.create(name="Lars", instrument="Drums", age=50)

    # 3) çoklu kaydetme
    #   musician_list = [Musician(name="Lars", instrument="Drums", age=50), Musician(name="Kirk", instrument="Bass", age=65)]
    #   Musician.objects.bulk_create(musician_list)

    # sınıf(table) oluşturduktan sonra bunları terminalde yazarak tablolara veri kaydedebiliriz.
