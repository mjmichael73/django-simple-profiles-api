from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from . import serializers
from profiles_api import models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        data = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'status': 'success', 'message': 'Hello', 'data': data})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"status": "success", "message": message})
        else:
            return Response(
                {"status": "false", "message": "Bad request", "data": {"errors": serializer.errors}},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        data = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'status': 'success', 'message': 'Hello', 'data': data})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"status": "success", "message": message})
        else:
            return Response(
                {"status": "false", "message": "Bad request", "data": {"errors": serializer.errors}},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self, request, pk=None):
        return Response({"method": "PUT"})

    def update(self, request, pk=None):
        return Response({"method": "PATCH"})

    def partial_update(self, request, pk=None):
        return Response({"method": "DELETE"})

    def destroy(self, request, pk=None):
        return Response({"method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
