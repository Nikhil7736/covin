from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from vaccine.models import booking


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        Password = request.POST.get('password1')
        Repeat_Password = request.POST.get('password2')
        email = request.POST.get('email')
        if Password == Repeat_Password:
            var_booking = booking(
                first_name=first_name,
                last_name=last_name,
                username=username,
                Password=Password,
                Repeat_Password=Repeat_Password,
                email=email,
            )
            var_booking.save()
            print("Booking Created", var_booking)
        return redirect('/')
    else:
        print("password not matching")
        return render(request, 'register.html')
