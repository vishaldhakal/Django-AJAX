from django.shortcuts import render, HttpResponse
from .models import userModel
from django.http import JsonResponse
import json
import matplotlib.pyplot as plt
import io
import urllib, base64
import csv


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

def plot(request):
    ticks = [0,1,2,3,4,5,6,7,8,9]
    labels = ['0B','1B','2B','3B','4B','5B','6B','7B','8B','9B']
    list1 = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]
    list2 = [2.3,3.5,4.7,3.5,3.8,3.0,5.0,5.1,6.7,7.1]
    plt.bar(list1,list2)
    plt.xlabel('Year in AD')
    plt.ylabel('Population')
    plt.title('Population growth as per year')
    plt.yticks(ticks, labels)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    base = base64.b64encode(buf.read())
    uri = urllib.parse.quote(base)
    return render(request,'home.html',{'data':uri})