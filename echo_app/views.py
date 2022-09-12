from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def private_chat(request, username):
    context = {
        'username_json':mark_safe(json.dumps(username))
    }
    return render(request, 'echo_app/private_chat.html',context)






















# def index(request):
#     return render(request,'echo_app/index.html')
#
# def room(request, room_name):
#     return render(request, 'echo_app/room.html', {
#         'room_name': room_name
#     })
