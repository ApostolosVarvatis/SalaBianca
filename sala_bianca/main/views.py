from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.http import JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from .models import Item, Contact, Reservation


# Private Event Form
class ReservationForm(forms.Form):
    first = forms.CharField(max_length=64)
    last = forms.CharField(max_length=64)
    email = forms.EmailField()
    phonenumber = forms.CharField(max_length=20)
    guests_num = forms.IntegerField(min_value=1)
    content = forms.CharField(widget=forms.Textarea, required=False)


# Contact Event Form
class ContactForm(forms.Form):
    first = forms.CharField(max_length=64)
    last = forms.CharField(max_length=64)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea, required=True)


# API Route
@csrf_exempt
def menu_item(request, item_title):
    try:
        item = Item.objects.get(title=item_title)
    except Item.DoesNotExist:
        return render(request, "main/error.html", {
            "error_msg" : "Trying to access non-existing item.",
            "error_code" : 404
        })

    if request.method == "GET":
        return JsonResponse(item.serialize())
    else:
        return render(request, "main/error.html", {
            "error_msg" : "GET request required for this route.",
            "error_code" : 400
        })



def index(request):
    return render(request, "main/index.html", {})
def test(request):
    return render(request, "main/test.html", {})


def error_404(request, exception):
    return render(request, "main/404.html", status=404)


def about(request):
    return render(request, "main/about.html", {})


def menu(request):
    items = Item.objects.all().order_by("title")
    return render(request, "main/menu.html", {"items" : items})

def beers(request):
    return render(request, "main/beers.html", {})
    
def cocktails(request):
    return render(request, "main/cocktails.html", {})
    
def wines(request):
    return render(request, "main/wines.html", {})
    
def coffees(request):
    return render(request, "main/coffees.html", {})
    
def teasjuices(request):
    return render(request, "main/teasjuices.html", {})
    
def beverages(request):
    return render(request, "main/beverages.html", {})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first"]
            last = form.cleaned_data["last"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            content = form.cleaned_data["content"]

            contact = Contact(
                first = first,
                last = last,
                email = email,
                subject = subject,
                content = content
            )
            contact.save()
            return render(request, "main/contact.html", {
                "form" : ContactForm(),
                "success_msg" : "Contact form was sent!"
            })
        else:
            return render(request, "main/contact.html", {
                "form" : form,
                "error_msg" : "Contact infromation was invalid! Please check again and resubmit."
            })

    return render(request, "main/contact.html", {"form" : ContactForm()})


def reservations(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)

        r_datetime_str = request.POST.get("reservation_datetime")
        try:
            r_datetime = parse_datetime(r_datetime_str)
        except ValueError:
            r_datetime = None

        if form.is_valid() and r_datetime:
            first = form.cleaned_data["first"]
            last = form.cleaned_data["last"]
            email = form.cleaned_data["email"]
            phonenumber = form.cleaned_data["phonenumber"]
            guests_num = form.cleaned_data["guests_num"]
            content = form.cleaned_data["content"]

            reservation_datetime = timezone.make_aware(r_datetime, timezone.get_current_timezone())

            reservation = Reservation(
                first = first,
                last = last,
                email = email,
                phonenumber = phonenumber,
                guests_num = guests_num,
                reservation_datetime = reservation_datetime,
                content = content
            )
            reservation.save()
            return render(request, "main/reservation.html", {
                "form" : ReservationForm(),
                "success_msg" : "Reservation form was sent!"
            })
        else:
            return render(request, "main/reservation.html", {
                "form" : form,
                "error_msg" : "Reservation infromation was invalid! Please check again and resubmit."
            })

    return render(request, "main/reservation.html", {"form" : ReservationForm()})

