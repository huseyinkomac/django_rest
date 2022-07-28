from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Default Game Serializer
    '''
    class Meta:
        model = Game
        fields = ['id', 'name', 'genre', 'release_date']
