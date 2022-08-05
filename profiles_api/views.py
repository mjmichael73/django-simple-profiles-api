from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        data = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'status': 'success', 'message': 'Hello', 'data': data})
