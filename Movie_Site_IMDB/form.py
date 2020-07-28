from django import forms
from User_Module.models import UserRegistrationModel

class UserRegistrationForm(forms.ModelForm):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'pattern':'^[a-zA-Z " " ]*$'}))
    email=forms.EmailField(label="Email")
    contactno=forms.IntegerField(label="Contact No.",widget=forms.NumberInput(attrs={'pattern':'^[7-9]{1}[0-9]{9}$'}))
    password=forms.CharField(label="Password")
    class Meta:
        fields="__all__"
        model=UserRegistrationModel
        