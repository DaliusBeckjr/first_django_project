from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file

app_name = 'surveys'

urlpatterns = [
    path('surveys/', views.index, name = 'index'),
    path('surveys/new', views.new, name = 'new'),
]
