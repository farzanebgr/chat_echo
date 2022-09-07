from django.urls import path
from echo_app import views

urlpatterns = [
    path('', views.index, name='index-page'),
]
