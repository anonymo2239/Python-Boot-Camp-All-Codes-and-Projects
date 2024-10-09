from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# binary field görsel eklemeye yarar.(SQL'de)

class Musician(models.Model):
    name = models.CharField(max_length=50) # çok uzun stringler için textfield kullanılır.
    # gerekli olan fieldları dökümandan okuyabilirsin.
    instrument = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)]) # aralık verebiliyoruz
    #sonradan ekleme yaparsak
    salary = models.IntegerField(default=1, validators=[MinValueValidator(0)]) # yapmalıyız ki hata vermesin veya null=True yapabiliriz
    
    def __str__(self):
        return f"Name: {self.name}, Instrument: {self.instrument}, Age: {self.age}, Salary:{self.salary}"
    # ilk önce makemigration'u çalıştırıp programı hazırlamalıyız. Sonra migrate'yi çalıştırmalıyız.
    # python manage.py makemigrations database_app
    # python manage.py migrate

    # MANAGE.PY I KULLANARAK TERMİNALDE BİR SHELL AÇABİLİRİZ (python manage.py shell -i ipython yazarsak jupyter
    # notebook gibi tek satirli kod yazabiliriz.)
    # settings.py'da INSTALLED_APPS'a 'database_app' eklemeyi unutma
    # from database_app.models import Musician'i eklemeyi unutma

    # INSERT
    # models kullanarak databes e veri kaydetme
    # 1) james = Musician(name="James", instrument="Drum", age=60)
    #    james.save() //burada bir satır kaydetmiş olduk(INSERT komutu gibi)

    # 2) Musician.objects.create(name="Lars", instrument="Drums", age=50)

    # 3) çoklu kaydetme
    #   musician_list = [Musician(name="Lars", instrument="Drums", age=50), Musician(name="Kirk", instrument="Bass", age=65)]
    #   Musician.objects.bulk_create(musician_list)

    # sınıf(table) oluşturduktan sonra bunları terminalde yazarak tablolara veri kaydedebiliriz.

    # SELECT
    # SORGULAR
    # Musician.objects.all() komutu o tablodaki tüm verileri gosterir.
    # Musician.objects.get(pk=2) komutu id'si 2 olanları getirir.
    # Musician.objects.get(name="James") komutu ismi james olan 'bir' kişiyi getirir.
    # get sadece bir sonuç getirir. ID için kullanılır.
    # birden fazla sonuç getirmek için filter() kullanılır.
    # Musician.objects.filter(instrument="Drum") komutu instrument'ı drum olanları getirir.

    # from django.db.models import Q yaparak daha ayrıntılı sorgular yapabiliyoruz. ve tek filter kullanmamız yetiyor
    # ORNEK 1: In [9]: Musician.objects.filter(Q(instrument='Drum')&Q(age=60)).all()
    #        Out[9]: <QuerySet [<Musician: Name: James, Instrument: Drum, Age: 60>]>

    # ORNEK 2: In [22]: Musician.objects.filter(Q(age__gte=60)).all() yasi 60 dan buyuk ve esit olanlar
              # Out [22]: <QuerySet [<Musician: Name: James, Instrument: Guitar, Age: 60>, <Musician: Name: Lars, Instrument: Drums, Age: 65>, <Musician: Name: Rob, Instrument: Bass, Age: 64>]>

              # In [23]: Musician.objects.filter(Q(age__gt=60)).all() yasi 60 dan buyuk olanlar
              # Out [23]: <QuerySet [<Musician: Name: Lars, Instrument: Drums, Age: 65>, <Musician: Name: Rob, Instrument: Bass, Age: 64>]>

              # In [24]: Musician.objects.filter(Q(name__endswith="s")).all() ismi 's' ile bitenler
              # Out [24]: <QuerySet [<Musician: Name: James, Instrument: Guitar, Age: 60>, <Musician: Name: Lars, Instrument: Drums, Age: 65>]>
    
    # UPDATE
    # In [9]: print(myrecord)
    # Out [11]: Name: Alperen, Instrument: Guitar, Age: 35, Salary: 100

    # In [10]: myrecord.name = "Baturalp"

    # In [11]: print(myrecord)
    # Out [11]: Name: Baturalp, Instrument: Guitar, Age: 35, Salary: 100

    # In [12]: myrecord.save()
    # eğer .save() yaparsak update komutunu uygulamış olacak.

    # DELETE
    # myrecord.delete() komutu ile siler.

