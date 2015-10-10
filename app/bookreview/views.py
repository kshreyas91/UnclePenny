from django.shortcuts import render
from rest_framework import generics
from bookreview.serializers import AuthorSerializer
from django.http import HttpResponse
from django.http import JsonResponse


from bookreview.models import Author

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)

def test_author(request):

	jsondata = AuthorSerializer(Author.objects.get(pk=1))
	return JsonResponse(jsondata.data)

class AuthorView(generics.ListAPIView):
    model = Author
    serializer_class = AuthorSerializer
