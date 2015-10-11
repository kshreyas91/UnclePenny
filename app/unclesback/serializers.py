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
        fields = ('id', 'first_name', 'last_name')


class StatusObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusObject
		fields = ('status', 'message')

