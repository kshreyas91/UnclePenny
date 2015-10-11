from rest_framework import serializers

from unclesback.models import (
    Author,
    Book,
    StatusObject,
)


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class StatusObjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = StatusObject
		fields = ('status', 'message')

