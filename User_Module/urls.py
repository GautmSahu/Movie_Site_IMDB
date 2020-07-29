"""Movie_Site_IMDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from User_Module import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_user_register/',views.show_user_register,name="show_user_register"),
    path('save_user_register/',views.save_user_register,name="save_user_register"),
    path('show_user_login/',views.show_user_login,name="show_user_login"),
    path('validate_user/',views.validate_user,name="validate_user"),
    path('search_movie/',views.search_movie,name="search_movie"),
    path('movie_page/',views.movie_page,name="movie_page"),
    path('user_watch_video/',views.user_watch_video,name="user_watch_video")
]
