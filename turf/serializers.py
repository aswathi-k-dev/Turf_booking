from rest_framework import serializers
from turf.models import Turf

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()



class TurfSerializer(serializers.Serializer):
    id = serializers.CharField(read_only = True)
    name = serializers.CharField()
    location = serializers.CharField()
    phone = serializers.CharField()
    fee = serializers.IntegerField()

    def validate(self,validated_data):
        fee = validated_data.get("fee")
        if fee < 100:
            raise serializers.ValidationError("invalid fee,fee should be > 100 ")
        return validated_data

