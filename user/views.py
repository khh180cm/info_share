from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User, Profile


class HelloView(APIView):
    '''Test the REST API'''
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, world'}
        return Response(content)
