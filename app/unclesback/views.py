from django.shortcuts import render
from rest_framework import generics
from bookreview.serializers import AuthorSerializer
from bookreview.serializers import StatusObjectSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
import sys
from bookreview.models import UserProfile
from bookreview.models import StatusObject


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
	test = []
	jsondata = AuthorSerializer(Author.objects.get(pk=1))
	return JsonResponse(jsondata.data)

@csrf_exempt
def test(request, u,v):
	print >>sys.stderr, request.POST.get('u','')
	# logging.error(request.POST)
	# test = "{'u': "+ request.POST.get['u',''] + " p: " + request.POST.get['p',''] + " }"
	# return JsonResponse(test)
	jsondata = AuthorSerializer(Author.objects.get(pk=1))
	return JsonResponse(jsondata.data)

def signup_user(request):
	username = request.GET.get('phonenumber', "")
	password = request.GET.get('password', "")
	firstname = request.GET.get('firstname', "")
	lastname = request.GET.get('lastname', "")
	bankname = request.GET.get('bankname', "")
	banknumber = request.GET.get('banknumber', "")
	user_profile = UserProfile.objects.create(firstname= firstname, lastname = lastname, password= password, banknumber=banknumber, bankname=bankname, username= username)
	user_profile.save()
	print >>sys.stderr, "User details saved"

	op_status = StatusObject.objects.create(status="success", message="User Created")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)





class AuthorView(generics.ListAPIView):
    model = Author
    serializer_class = AuthorSerializer
