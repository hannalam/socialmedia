from django.db import models

# I wrote this code

from django.conf import settings

# model for profile set up


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # show the user's username in the admin page
    def __str__(self):
        return self.user.username

# model for friend list set up


class FriendList(models.Model):

    # show the user's username in the admin page
    def __str__(self):
        return self.user.username

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    nickname = models.SlugField(max_length=100, blank=True)

# end of code I wrote
