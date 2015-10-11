from rest_framework import serializers

from unclesback.models import (
    UserProfile,
    Challenge,
    Team,
    ActivityFeed,
    StatusObject,
)


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('id', 'firstname', 'lastname','currentChallenge','currentsavings','futureestimate')

class StatusObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusObject
		fields = ('status', 'message')

class ChallengeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Challenge
		fields = ('id','challenge_name','challenge_details','start_date','end_date') 

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = ('id','team_name','status')



