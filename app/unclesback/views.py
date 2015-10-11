from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from unclesback.models import UserProfile
from unclesback.models import StatusObject
from unclesback.models import Challenge
from unclesback.serializers import *
from unclesback.models import ActivityFeed
from unclesback.models import Team

import logging
import sys


def index_view(request):
    response = {
    UserProfile.objects.all()
    }
    return render(request, 'index.html', response)

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
	op_status = StatusObject.objects.create(status="success", message="User Created")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)


def login_user(request):
	u_username = request.GET.get('username', "")
	u_password = request.GET.get('password', "")
	userObject = UserProfile.objects.get(username=u_username)
	if userObject is None:
		op_status = StatusObject.objects.create(status="failed", message="User Doesnt Exist")
	else:
		if userObject.password == u_password:
			op_status = StatusObject.objects.create(status="success", message=userObject.firstName + ":" + userObject.username)
		else:
			op_status = StatusObject.objects.create(status="failed", message="Username and password doesnt match")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

	

