from django.shortcuts import render, redirect
from AmbulanceApp.models import User
from AmbulanceApp.models import Ambulance
from AmbulanceApp.forms import UserForm, AmbulanceForm
#import auth for authentication
from django.contrib import messages ,auth 
# import login_required decorator
from django.contrib.auth.decorators import login_required



# Create your views here.


def user_register(request):
    if request.method == 'POST':
        user = User(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                    username=request.POST['username'], password=request.POST['password'])
        user.save()
        return redirect('/user_login')
    else:
        return render(request, 'user_register.html')


def user_login(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=uname,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
        
    return render(request, 'user_login.html')


def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'update_profile.html', {'user': user})


def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect('/about')
    else:
        return render(request, 'update_profile.html', {'user': user})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

#use login required decorator to prevent access to the page without login
#use login_url to redirect to login page if the person has not logged in 

@login_required(login_url='/user_login')
def ambulance(request):
    ambulances = Ambulance.objects.all()
    return render(request, 'ambulances.html', {'ambulance': ambulances})


def booked(request):
    return render(request, 'booked_ambulances.html')


def hospitals(request):
    return render(request, 'nearby_hospitals.html')


def services(request):
    return render(request, 'services.html')


def update_profile(request):
    return render(request, 'update_profile.html')


def ambulance_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        Ambulance_No = request.POST.get('Ambulance_No')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        Phone_number = request.POST.get('Phone_number')
        Gender = request.POST.get('Gender')
        Ambulance_type = request.POST.get('Ambulance_type')
        Status = request.POST.get('Status')

        driver = Ambulance.objects.create(
            firstname=firstname,
            lastname=lastname,
            age=age,
            Ambulance_No=Ambulance_No,
            email=email,
            username=username,
            password=password,
            Phone_number=Phone_number,
            Gender=Gender,
            Ambulance_type=Ambulance_type,
            Status=Status,
        )
        # You can perform additional actions if needed, e.g., redirect to a success page.
        return redirect('/ambulance_login')

    return render(request, 'ambulance_register.html')


def ambulance_login(request):
    return render(request, 'ambulance_login.html')


def booking_request(request):
    return render(request, 'booking_request.html')


def emergency_booking(request):
    return render(request, 'emergency_booking.html')


def ambulance_status(request):
    return render(request, 'ambulance_status.html')


def near_hospitals(request):
    return render(request, 'near_hospitals.html')


def driver_profile(request):
    return render(request, 'driver_profile.html')
