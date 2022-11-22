from django.shortcuts import render
from . import models

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python !'},
#     {'id': 2, 'name': 'Lets learn Java !'},
#     {'id': 3, 'name': 'Lets learn Cloud !'},
#     {'id': 4, 'name': 'Lets learn C++ !'}
# ]

def home(request):
    rooms = models.Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = models.Room.objects.get(id=pk)

    context = {'room': room}

    return render(request, 'base/room.html', context)
