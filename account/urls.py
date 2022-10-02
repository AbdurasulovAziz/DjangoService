from django.urls import path, include
from account import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('', include("django.contrib.auth.urls"), name='login'),

]