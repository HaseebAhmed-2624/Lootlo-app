from api.models import CustomUser, UserType
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


@api_view(['POST'])
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password],
                                     style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    city = serializers.CharField(max_length=30, required=True)
    address = serializers.CharField(max_length=100, required=True)
    postal_code = serializers.IntegerField(required=True)
    user_type = UserTypeSerializer(many=True)

    # usertype=serializers.
    class Meta:
        user = get_user_model()
        model = user
        fields = (
            'username', 'password', 'password2', 'email', 'first_name', 'last_name', 'address', 'city', 'postal_code')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'required': False}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            city=validated_data['city'],
            postal_code=validated_data['postal_code'],
        )
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.city = validated_data.get('city', instance.city)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
        return instance
