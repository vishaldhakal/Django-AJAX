from django.shortcuts import render, HttpResponse
from .models import userModel
from django.http import JsonResponse
import json


def index(request):
    userobj = userModel.objects.all()
    context = {'users':userobj}
    return render(request,'index.html',context)

def crud_ajax_create(request):
    name = request.GET['name']
    email = request.GET['email']
    age = request.GET['age']
    us = userModel(name=name,email=email,age=age)
    us.save()
    l = list()
    data = {
        'name': name,
        'email': email,
        'age': age,
    }
    l.append(data)
    return HttpResponse(json.dumps(l))
