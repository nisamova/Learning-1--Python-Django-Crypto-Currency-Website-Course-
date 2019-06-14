#NSI Created this for your new app called crypto according to convention
from django.urls import path
from .import views 
urlpatterns = [
    path('', views.home, name="home"),
]
