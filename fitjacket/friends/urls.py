from django.urls import path
from . import views

urlpatterns = [
    path('', views.social, name='friends.social'),
]