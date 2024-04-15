def uslu_sayilar(a, b):
    i = 0
    sayi = 1
    while(i < b):
        sayi *= a
        i = i + 1
    print("Cevap:",sayi)

x = int(input("Tabanı giriniz: "))
y = int(input("Üssü giriniz: "))

uslu_sayilar(x, y)