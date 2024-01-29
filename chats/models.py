from django.db import models

# I wrote this code

from django.contrib.auth.models import User

# model for chatroom setup


class ChatRoom(models.Model):

    # show the chatroom name in the admin page
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

# model for chatroom message setup


class ChatRoomMessage(models.Model):

    # show the messages in the admin page
    def __str__(self):
        return self.messages

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    messages = models.TextField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('date',)

# end of code I wrote
