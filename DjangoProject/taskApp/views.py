import re
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,models,login

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import userSerialiser
from .models import userData
from django.contrib import messages

def index(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(user)
            return redirect("/account",username=username)

    return render(request,"index.html")


@api_view(['POST'])
def addUser(request):
    serializer = userSerialiser(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return redirect('http://127.0.0.1:8000/signup/')
    return redirect("/")

@api_view(['GET'])
def searchUser(request,user,email):
    tasks = userData.objects.get(userName=user,email=email)
    serializer = userSerialiser(tasks, many=False)
    if serializer is not None:
        context={
            "user":user
        }
        return render(request,"newPass.html",context)

@api_view(['POST'])
def updatePass(request,user):
	task = userData.objects.get(userName=user)
	serializer = userSerialiser(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(request.data)


def signup(request):
    return render(request,"signup.html")

def forgot(request):
    return render(request,"forgot.html")

