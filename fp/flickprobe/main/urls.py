from django.contrib import admin
from django.urls import path , include
from . import views

app_name="main"
urlpatterns = [
    path("",views.home,name='home'),
    path("detail/<int:id>",views.detail,name='detail'),
    path("AboutUs",views.about_us,name='AboutUs'),
    path("Language/<str:L>",views.Lang,name='Language')

 ]