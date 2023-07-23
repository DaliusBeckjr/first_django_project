from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file

app_name = 'blogs'

urlpatterns = [
    path('', views.root, name = 'root'),
    path('blogs/', views.index, name = 'index'), # localhost:8000/blogs
    path('blogs/news', views.new, name = 'new'),
    path('blogs/create', views.create, name = 'create'),
    path('blogs/<number>', views.show, name = 'show'),
    path('blogs/<number>/edit', views.edit, name = 'edit'),
    path('blogs/<number>/delete', views.delete, name = 'delete'),
]
