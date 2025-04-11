from django import forms
from AmbulanceApp.models import User, Ambulance


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname', 'email', 'username', 'password', 'Phone_number', 'Gender']


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = ['id', 'firstname', 'lastname', 'age', 'email', 'username', 'password', 'Phone_number', 'Gender', 'Ambulance_No', 'Ambulance_type', 'Status']

