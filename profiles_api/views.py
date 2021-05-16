from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from profiles_api import serializers
from rest_framework.response import Response

from profiles_api import serializers
from rest_framework import status

# Create your views here.
class HelloApiView(APIView):
    """ Learning how to call """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP Methods as functions(get, post, update, patch, delete)',
            'Is similar to a traditonal Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLS'
        ]

        return Response({ 'message': 'Hello World!', 'an_apiview': an_apiview })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({ 'message': message })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """ update profiles """
        return Response({ 'method': 'PUT' })

    def patch(self, request, pk=None):
        """ patch profile """
        return Response({ 'method': 'PATCH' })

    def delete(self, request, pk=None):
        """ delete profile """
        return Response({ 'method': 'DELETE' })

    


# viewsets
class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update, destroy',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({ 'message': 'Hello World..', 'a_viewset': a_viewset })

    
    def create(self, request):
        """ Write logic here """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name} !"
            return Response({ 'message': message })

    
    def retrieve(self, request, pk=None):
        """ retrieve a specific object """
        return Response({ 'http_method': 'GET' })

    
    def update(self, request, pk=None):
        """ update a specific object """
        return Response({ 'http_method': 'PUT' })

    
    def partial_update(self, request, pk=None):
        """ partially update a specific object """
        return Response({ 'http_method': 'PATCH' })

    def destroy(self, request, pk=None):
        """ Delete Specific objects """
        return Response({ 'http_method': 'DELETE' })