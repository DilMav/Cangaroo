from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('contacts', views.contacts),
    path('cabinet', views.cabinet),
]