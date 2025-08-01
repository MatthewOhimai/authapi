from rest_framework import serializers   #  "To convert the model intsance to json, etc."
from .models import User, Profile        #  "Importing User and profile"
from rest_framework.validators import UniqueValidator
import re

"Serializer for Profile"
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'role', 'date_of_birth']

    "Validating phoe number according to nigeria phone number e.g 08166778899"
    def validate_phone_number(self, value):
        if not re.match(r'^0\d{10}$', value):
            raise serializers.ValidationError("Input a correct phone number.")
        return value

"Serializer for User"
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    "To make sure email is in a valid format"
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    "Used write_only-true so that password won't be exposed in api, list the model fields that should be serialized"
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    "Usageof pop so that validated data now only has field relasted to user"
    def create(self, validated_data):   # Overides the create method of the DRF serializers
        profile_data = validated_data.pop('profile')   # Extract profile from validated data
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)  # Created a new user instance 
        user.set_password(password)  # hashes the passoword and link it to user
        user.save()
        Profile.objects.create(user=user, **profile_data) # created a profile nstance for user
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['profile'] = ProfileSerializer(instance.profile).data
        return rep
    