from django.shortcuts import render

# def index(request):
#     return render(request,'echo_app/index.html')
#
# def room(request, room_name):
#     return render(request, 'echo_app/room.html', {
#         'room_name': room_name
#     })

def private_chat(request, username):
    return render(request, 'echo_app/private_chat.html',{'username':username})