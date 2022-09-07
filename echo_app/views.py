from django.shortcuts import render

def index(request):
    return render(request,'echo_app/index.html')