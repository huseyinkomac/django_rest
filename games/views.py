from django.shortcuts import render
from django.http import Http404

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game
from .serializers import GameSerializer


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    '''
    Game Viewset
    Retrieve all objects and serialize
    '''
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameListView(APIView):
    '''
    GameList View
    Listing all the games
    '''
    def get(self, request, format=None):
        '''
        Returning all games saved in db
        '''
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GameCreateView(APIView):
    '''
    GameCreate View
    Create a new game with all fields
    '''
    def post(self, request, format=None):
        '''
        Create a new game. All fields required
        '''
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetailView(APIView):
    '''
    GameDetail View
    With given id several processes can be made to that game
    @get - get
    @put - update
    @delete - delete
    '''
    def get_object(self, pk):
        '''
        Get game object with it's pk. raise 404 if not found
        Acts like a decorator
        '''
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        Get a game with id
        '''
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        '''
        Update a game with given id. All fields required
        '''
        game = self.get_object(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''
        Delete a game with given id
        '''
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
