from django.shortcuts import render
from rest_framework import generics
from unclesback.serializers import UserSerializer
from django.http import HttpResponse
from django.http import JsonResponse


from unclesback.models import User
from unclesback.models import Challenge
from unclesback.models import ActivityFeed
from unclesback.models import Team

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'users': User.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)

def test_users(request):
    jsondata = UserSerializer(User.objects.all())
    return JsonResponse(jsondata.data)

class UserView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
