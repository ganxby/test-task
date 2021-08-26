from django.contrib import admin
from django.urls import path, include

from mainapp import views
from mainapp.views import main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('api/users/', views.UserList.as_view()),
    path('api/', include('mainapp.urls')),

]
