from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),

    path('users/', views.index, name= 'index'),
    path('users/new', views.new, name = 'new'),
]
