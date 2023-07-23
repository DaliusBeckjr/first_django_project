from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def register(request):
    # register would be a page that has the register form 
    # render (request, register.html) for example
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def index(request):
    return HttpResponse("placeholder to later display all the list of users")

def new(request):
    # new user would be the form on the register page that is linked to a post method
    # print("Got Post info........")
    # print(request.POST)
    # return render(request, "index.html") # take the new user to the blogs dashboard
    pass