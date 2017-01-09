from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="accounts:user-detail")

	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name="accounts:group-detail")

	class Meta:
		model = Group
		fields = ['url', 'name']
