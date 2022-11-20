from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn Python !'},
    {'id': 2, 'name': 'Lets learn Java !'},
    {'id': 3, 'name': 'Lets learn Cloud !'},
    {'id': 4, 'name': 'Lets learn C++ !'}
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request):
    return render(request, 'room.html')
