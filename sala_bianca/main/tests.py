from django.test import Client, TestCase

from .models import Contact, Reservation

#import os
#import pathlib
#from selenium import webdriver


# Create your tests here.

# Test Models
class ContactTestCase(TestCase):
        
    def test_valid_contact(self):
        cf = Contact.objects.create(
            first="John",
            last="Doe",
            email="john@example.com",
            subject="Test Subject",
            content="Test content"
        )
        self.assertTrue(cf.is_valid_contact_form())

    def test_invalid_contact_email(self):
        cf = Contact.objects.create(
            first="John",
            last="John",
            email="johnexample.com",
            subject="Test Subject",
            content="Test content"
        )
        self.assertFalse(cf.is_valid_contact_form())

    def test_invalid_contact_first_last_name(self):
        cf = Contact.objects.create(
            first="John",
            last="John",
            email="john@example.com",
            subject="Test Subject",
            content="Test content"
        )
        self.assertFalse(cf.is_valid_contact_form())

class ReservationTestCase(TestCase):

    def test_valid_reservation(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Doe",
            email="jane@example.com",
            phonenumber="123-456-7890",
            guests_num=4,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )
        self.assertTrue(rf.is_valid_reservation_form())

    def test_invalid_reservation_email(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Doe",
            email="janeexample.com",
            phonenumber="123-456-7890",
            guests_num=4,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )
        self.assertFalse(rf.is_valid_reservation_form())

    def test_invalid_reservation_first_last_name(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Jane",
            email="jane@example.com",
            phonenumber="123-456-7890",
            guests_num=4,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )
        self.assertFalse(rf.is_valid_reservation_form())

    def test_invalid_reservation_phonenumber(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Doe",
            email="jane@example.com",
            phonenumber="123456",
            guests_num=4,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )
        self.assertFalse(rf.is_valid_reservation_form())

    def test_invalid_reservation(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Doe",
            email="jane@example.com",
            phonenumber="123-456-7890",
            guests_num=3,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )
        self.assertFalse(rf.is_valid_reservation_form())

    def test_invalid_reservation(self):
        rf = Reservation.objects.create(
            first="Jane",
            last="Doe",
            email="jane@example.com",
            phonenumber="123-456-7890",
            guests_num=101,
            reservation_datetime="2023-08-29 14:00:00",
            content="Test reservation content"
        )

        self.assertFalse(rf.is_valid_reservation_form())

# Test Webpages
class WebpagesTestCase(TestCase):

    def test_index(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)

    def test_error_page(self):
        c = Client()
        response = c.get("/aa")
        self.assertEqual(response.status_code, 404)

    def test_contact_page(self):
        c = Client()
        response = c.get("/contact")
        self.assertEqual(response.status_code, 200)

    def test_reservation_page(self):
        c = Client()
        response = c.get("/reservations")
        self.assertEqual(response.status_code, 200)


# Selenium tests
"""
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()

class WebpageTests(unittest.TestCase):
    def test_index_title(self):
        driver.get(file_uri("index.html"))
        self.assertEqual(driver.title, "Sala Bianca")

    def test_menu_title(self):
        driver.get(file_uri("menu.html"))
        self.assertEqual(driver.title, "Menu")

    def test_menu_button(self):
        driver.get(file_uri("index.html"))
        btn = driver.find_element_by_id("responsiveButton")
        menu = driver.find_element_by_id("menu-wrap")
        btn.click()
        self.assertTrue("open" in btn.get_attribute("class"))
        self.assertTrue("open-menu" in menu.get_attribute("class"))
        btn.click()
        self.assertTrue("open" not in btn.get_attribute("class"))
        self.assertTrue("open-menu" not in menu.get_attribute("class"))
"""