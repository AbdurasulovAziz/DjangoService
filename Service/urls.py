from django.urls import path
from Service import views

urlpatterns = [
    path('', views.home, name='home'),
]