# I wrote this code

from rest_framework import serializers
from .models import *

# serialize the profile and friendlist input


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'photo']


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = ['user', 'nickname']

# end of code I wrote
