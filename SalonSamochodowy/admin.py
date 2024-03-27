from django.contrib import admin

from .models import CarList

from .models import Book

# Register your models here.
admin.site.register(CarList)
admin.site.register(Book)
