from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn Python !'},
    {'id': 2, 'name': 'Lets learn Java !'},
    {'id': 3, 'name': 'Lets learn Cloud !'},
    {'id': 4, 'name': 'Lets learn C++ !'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i

    context = {'room': room}

    return render(request, 'base/room.html', context)
