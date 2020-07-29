from django.shortcuts import render,redirect
from Movie_Site_IMDB.form import UserRegistrationForm
from User_Module.models import UserRegistrationModel
import json
import requests
from bs4 import BeautifulSoup

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
    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
    }
    response = requests.request("GET", url + search, headers=headers)
    # print(response.text)
    result=json.loads(response.text)
    # print(type(result))
    # for key1,value1 in result.items():
    #     print(key1,"--------->",value1)
    #     for data in value1:
    #         print(data)
    return render(request,"index.html",{"result":result,"search_for":search})


def movie_page(request):
    m_id=request.GET.get("idno")
    print(m_id)
    url = "https://imdb8.p.rapidapi.com/title/get-videos"

    querystring = {"limit": "25", "region": "US", "tconst": m_id}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "83606917f9msh6544cdfbd9b7104p1c694fjsn04e02b46f998"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result=json.loads(response.text)
    print(result)
    print(type(result))
    for key1,val1 in result.items():
        if key1 == "resource":
            print(key1,"------>",val1)
            for key2,val2 in val1.items():
                print(key2,"--->",val2)
                if key2 == "image":
                    for key9, val9 in val2.items():
                        print(key9, "-->", val9)
                if key2=="videos":
                    for list_data in val2:
                        print(list_data)
                        for key3,val3 in list_data.items():
                            print(key3,"---->",val3)
                            if key3=="image":
                                for key4,val4 in val3.items():
                                    print(key4,"--->",val4)
                            if key3=="primaryTitle":
                                for key5,val5 in val3.items():
                                    print(key5,"--->",val5)
                                    if key5=="image":
                                        for key6,val6 in val5.items():
                                            print(key6,"--->",val6)
                            if key3=="parentTitle":
                                for key7,val7 in val3.items():
                                    print(key7,"-->",val7)
                                    if key7=="image":
                                        for key8,val8 in val7.items():
                                            print(key8,"-->",val8)
    return render(request,"usr/search_details.html",{"details":result})


def user_watch_video(request):
    vid=str(request.GET.get("vid"))
    print(vid)
    original_id=vid.split('/')
    print(original_id)
    url="https://www.imdb.com/video/"
    response=requests.get(url+original_id[2],None)
    print(response.status_code)
    print(response.text)
    bs=BeautifulSoup(response.text,"lxml-xml")
    res=bs.find("div",{"class":"jw-media jw-reset"})
    print("printing ",res.text)
