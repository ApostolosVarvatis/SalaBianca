from django.contrib import admin

from .models import Category, Item, Contact, Reservation
# Register your models here.

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Contact)
admin.site.register(Reservation)