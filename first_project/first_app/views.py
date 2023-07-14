from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    # redirect this to '/blogs'
    return redirect("/blogs")

def blogs(request):
    return HttpResponse('hello')

def new_blog(request):
    pass

def create_blog(request):
    pass

def number_blog(request):
    pass

def edit_blog(request):
    pass

def delete_blog(request):
    pass

def json_blog(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})