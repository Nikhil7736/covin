from django.shortcuts import render, redirect

# Create your views here.
from vaccine.models import booking


def home(request):
    return render(request, 'home.html')


def view_login(request):
    return render(request, 'login.html')


def login(request):
    Password = request.POST.get('password')
    email = request.POST.get('email')
    # print('all',booking.objects.all())
    var_booking = booking.objects.filter(
        Password=Password,
        email=email
    ).first()

    print(request.POST, var_booking)
    if var_booking is not None:
        return render(request, 'register.html')

    return redirect('/')
