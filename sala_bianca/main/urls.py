from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("menu", views.menu, name="menu"),
    path("reservations", views.reservations, name="reservations"),
    path("contact", views.contact, name="contact"),
    path("cocktails", views.cocktails, name="cocktails"),
    path("beers", views.beers, name="beers"),
    path("wines", views.wines, name="wines"),
    path("coffees", views.coffees, name="coffees"),
    path("teasjuices", views.teasjuices, name="teasjuices"),
    path("beverages", views.beverages, name="beverages"),
    

    # API Route
    path("menu/<str:item_title>", views.menu_item, name="menu_item")
]