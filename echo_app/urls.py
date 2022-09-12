from django.urls import path
from echo_app import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<str:room_name>/', views.room, name='room'),
    path('<str:username>/', views.private_chat, name='private-chat')
]