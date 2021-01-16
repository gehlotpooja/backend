from rest_framework import serializers
from .models import *
class GetLobbyDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = LobbyDetails
        fields = ('id','name','entry_fee','house_charges')