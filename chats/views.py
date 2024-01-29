from django.shortcuts import render

# I wrote this code

from .models import ChatRoom


# Chat room main page
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chats/chatrooms.html', {'chatrooms': chatrooms})


# Individual chat room page
def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request, 'chats/chatroom.html', {'chatroom': chatroom})

# end of code I wrote
