from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListRetrieveSerializer(serializers.ModelSerializer):    # serializer для ModelViewSet

    user = UserSerializer()                                       # берет поле user из модели Post

    class Meta:
        model = Post
        fields = '__all__'