from rest_framework import serializers

from unclesback.models import (
    Team,
    Challenge,
    User,
    ActivityFeed
)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id')

class TeamSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Team
        fields = ('id', 'members', 'status')

class ChallengeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Challenge
        fields = ('id', 'challenge_name', 'challenge_details','start_date','end_date')
  
class ActivityFeedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityFeed
        fields = ('id')
