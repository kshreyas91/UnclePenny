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
        fields = ('id', 'firstname', 'lastname')


class StatusObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusObject
		fields = ('status', 'message')


class ChallengeSerisalizer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('challenge_name','challenge_details')