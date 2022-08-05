"""
Serializers for prispevok APIs
"""
import requests
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Prispevok


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Prispevok
        fields = ['author', 'body', 'title']

    def create(self, validated_data):
        user_id = self.initial_data['author']
        if User.objects.filter(id=user_id).exists():
            return Prispevok.objects.create(**validated_data)
        else:
            url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
            r = requests.get(url, headers={'Content-Type': 'application/json'})
            j_user = r.json()
            if j_user:
                return Prispevok.objects.create(**validated_data)
            else:
                raise ValueError('User doesnt exist')


class PostSerializer(ModelSerializer):

    class Meta:
        model = Prispevok
        fields = ['id', 'body', 'title']

    def update(self, instance, validated_data):
        instance.body = validated_data.get('body', instance.body)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
