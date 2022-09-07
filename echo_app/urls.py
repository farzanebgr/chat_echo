from django.urls import path
from echo_app import views
urlpatterns = [
    path('admin/', views.index, name='index-page'),
]
