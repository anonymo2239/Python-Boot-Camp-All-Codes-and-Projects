#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Django, web uygulamalarını hızlı ve verimli bir şekilde geliştirmek için kullanabileceğiniz bir yazılımdır.

# django-admin startproject django_learning_project komutu Django'da yeni bir proje oluşturmak için kullanılır. Bu komut, Django projesi için gerekli olan dosyaları ve klasörleri oluşturur.
# manage.py dosyası, Django projesiyle etkileşimde bulunmak için kullanılan bir komut satırı aracıdır. manage.py dosyası, Django projesinin yönetim görevlerini gerçekleştirmek için kullanılır.

# python manage.py runserver komutu, Django projesini çalıştırmak için kullanılır. Bu komut, Django projesini yerel bir sunucuda çalıştırır ve projenin çalıştığı URL'yi gösterir.
# python manage.py runserver yazdığımızda http://127.0.0.1:8000/ adresine giderek projemizi görebiliriz. Bu bizim web sitesi adresimizdir. Sunucu çalıştığı sürece bu adrese giderek projemizi görebiliriz.

# Bir projenin içinde birden fazla app olabilir. Django'da bir app oluşturmak için python manage.py startapp app_adı komutunu kullanabiliriz.
# Sadece bir app in içinde de çalışabiliriz veya sonradan birden fazla app oluşturabiliriz. Django bu yüzden scalable bir yapıya sahiptir.

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_learning_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
