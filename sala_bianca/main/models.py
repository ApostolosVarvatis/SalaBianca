from django.db import models


# Created models are here.

class Category(models.Model):
    name = models.CharField(max_length=64)

class Item(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "image": self.image,
            "description": self.description,
            "category": self.category
        }

class Contact(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)

    def is_valid_contact_form(self):
        return self.first != self.last and '@' in self.email

class Reservation(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=20)
    guests_num = models.PositiveIntegerField()
    content = models.TextField(blank=True)
    reservation_datetime = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid_reservation_form(self):
        return self.first != self.last and '@' in self.email and len(self.phonenumber) >=7 and 4 <= self.guests_num <= 100