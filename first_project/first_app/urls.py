from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index), # this is root

    path('blogs', views.blogs), # localhost:8000/blogs
    path('blogs/new', views.new_blog), #localhost:8000/blogs/new
    path('blogs/create', views.create_blog),
    path('blogs/<number>', views.number_blog),
    path('blogs/<number>/edit', views.edit_blog),
    path('blogs/<number>/delete', views.delete_blog),
    # bonus
    path('blogs/json', views.json_blog),
]

