from rest_framework import generics

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from unclesback.models import *
from unclesback.serializers import *

import logging
import sys
import json
from django.core.serializers.json import DjangoJSONEncoder


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


#User Sign Up
def signup_user(request):
	username = request.GET.get('username', "")
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

#User Sign up Ends


# Challege CRUD Operations

def listChallenges(request):
	challenges = Challenge.objects.get(id=1)
	jsonData = ChallengeSerializer(challenges)
	return JsonResponse(jsonData)

def listSingleChallenge(request):
	challenges = Challenge.objects.filter(is_single=1)
	jsonData = ChallengeSerializer(challenges)
	return JsonResponse(jsonData.data, safe=False)

def listGroupChallege(request):
	challenges = Challenge.objects.filter(is_single=1)
	jsonData = ChallengeSerializer(challenges)
	return JsonResponse(jsonData.data, safe=False)


def addNewChallege(request):
	challenge_name = request.GET.get('name', "")
	challenge_details = request.GET.get('details', "")
	start_date = request.GET.get('sdate', "")
	end_date = request.GET.get('edate', "")
	is_single = request.GET.get('type', 1)
	challengeTuple = Challenge.objects.create(challenge_name= challenge_name, challenge_details= challenge_details, start_date=start_date,end_date=end_date,is_single=is_single)
	challengeTuple.save()
	op_status = StatusObject.objects.create(status="success", message="Challenge Created")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

# Challege CRUD Operations END

# Team CRUD Operations 

def addNewTeam(request):
	team_name = request.GET.get('name', "")
	challenge_id = request.GET.get('cid', "")
	teamTuple = Team.objects.create(team_name= team_name, challenge_id=challenge_id)
	teamTuple.save()
	op_status = StatusObject.objects.create(status="success", message="Team Created")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

def joinTeam(request):
	userid = request.GET.get('userid', "")
	teamid = request.GET.get('teamid', "")
	teamMemberTuple = TeamMember.object.create(userid= userid, teamid= teamid)
	teamMemberTuple.save()

	teamRow = Team.objects.get(id=teamid)
	challengeId = teamRow.challenge_id

	userRow = UserProfile.objects.get(id=userid)
	userRow.currentChallenge = challengeId
	userRow.save()

	op_status = StatusObject.objects.create(status="success", message="You have succesfully joined a team")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

def listAllTeamForChallenge(request):
	challengeId = request.GET.get('cid','')
	teamArray = Team.objects.filter(challenge_id = challengeId)
	jsondata = TeamSerializer(teamArray)
	return JsonResponse(jsondata.data, safe=False)

# Team CRUD Operations ENDS


# Take up individual challenge 

def enrollSingleChallenge(request):
	userid = request.GET.get('userid', '')
	challenge_id = request.GET.get("cid","")
	singleChallengeEnrollTuple = SingleChallegeMemebers.objects.create(userid=userid,challenge_id=challenge_id)
	singleChallengeEnrollTuple.save()

	userRow = UserProfile.objects.get(id=userid)
	userRow.currentChallenge = challenge_id
	userRow.save()

	op_status = StatusObject.objects.create(status="success", message="You have succesfully taken up a challenge")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

# Take up individual challenge ENDS


# Get user's current Challenge 

def  getUsersCurrentChallenge(request):
	userid = request.GET.get('userid','')
	singleChallenge = SingleChallegeMemebers.objects.filter(userid=userid)
	teamChallenge = TeamMembers.objects.filter(userid= userid)
	if not singleChallenge and not teamChallenge:
		op_status = StatusObject.objects.create(status="failed", message="No Current Challenges")
		jsondata = StatusObjectSerializer(op_status)
		return JsonResponse(jsondata.data)
	else:
		if(teamChallenge):
			teamid = teamChallenge[0].teamid
			teamTuple = Team.objects.filter(id=teamid)
			challenge_id = teamTuple[0].challenge_id
			challengeTuple = Challenge.objects.filter(id=challenge_id)

			jsondata = ChallengeSerializer(challengeTuple[0])
			return JsonResponse(jsondata.data, safe=False)
		else:
			challenge_id = singleChallenge[0].challenge_id
			challengeTuple = Challenge.objects.filter(id=challenge_id)
			jsondata = ChallengeSerializer(challengeTuple[0])
			return JsonResponse(jsondata.data, safe=False)

# Get user's current Challenge - END


# User Login
def login_user(request):
	u_username = request.GET.get('username', "")
	u_password = request.GET.get('password', "")
	userObject = UserProfile.objects.filter(username=u_username)
	if userObject is None:
		op_status = StatusObject.objects.create(status="failed", message="User Doesnt Exist")
	else:
		if userObject[0].password == u_password:
			jsondata = UserProfileSerializer(userObject[0])
			return JsonResponse(jsondata.data)
		else:
			op_status = StatusObject.objects[0].create(status="failed", message="Username and password doesnt match")
	jsondata = StatusObjectSerializer(op_status)
	return JsonResponse(jsondata.data)

# User Login Ends
	

