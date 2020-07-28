from django.shortcuts import render,redirect
from Movie_Site_IMDB.form import UserRegistrationForm
from User_Module.models import UserRegistrationModel
import json

# Create your views here.
def show_user_register(request):
    return render(request,"usr/user_registration.html",{"reg_form":UserRegistrationForm()})


def save_user_register(request):
    uf=UserRegistrationForm(request.POST)
    if uf.is_valid():
        uf.save()
        return render(request,"usr/user_registration.html",{"success":"Registration Successfull","reg_form":UserRegistrationForm()})
    else:
        return render(request,"usr/user_registration.html",{"error":uf.errors,"reg_form":UserRegistrationForm()})


def show_user_login(request):
    return render(request,"usr/user_login.html")


def validate_user(request):
    email=request.POST.get("email")
    pwd=request.POST.get("password")
    try:
        UserRegistrationModel.objects.get(email=email,password=pwd)
        request.session["uname"]=email
        print(request.session.get('uname'))
        return redirect('main')
    except UserRegistrationModel.DoesNotExist:
        return render(request,"usr/user_login.html",{"error":"Invalid Credentials"})


def search_movie(request):
    search=request.GET.get("search_movie")

    import requests
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
    }

    response = requests.request("GET", url + search, headers=headers)
    # print(url + search)
    print(response.text)
    result=json.loads(response.text)
    print(type(result))
    for key1,value1 in result.items():
        print(key1,"--------->",value1)
        for data in value1:
            print(data)
    return render(request,"index.html",{"result":result,"search_for":search})
