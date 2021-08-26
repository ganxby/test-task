from django.shortcuts import render
from rest_framework import generics

from rest_framework import viewsets

from .models import User, Post
from . import serializers
from .serializers import (
    UserSerializer,
    PostSerializer,
    PostListRetrieveSerializer
)


################ imports end ################

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

def main_page(request):
    return render(request, 'mainPg.html')

################ below nesting ################

class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    action_to_serializer = {                    # action для get_serializer_class
        'list': PostListRetrieveSerializer,
        'retrieve': PostListRetrieveSerializer
    }

    def get_serializer_class(self):             # вывод данных об авторе вместо его id
        return self.action_to_serializer.get(   #
            self.action,                        # (вывод action_to_serializer первым)
            self.serializer_class               # (вывод serializer_class, если нет action_to_serializer)
        )