from django.urls import path
from .views import PostListViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register('posts', PostListViewSet, basename = 'Posts')

urlpatterns = [

]

urlpatterns += router.urls