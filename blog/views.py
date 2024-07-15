from django.shortcuts import render,HttpResponse
import requests
# Create your views here.

def bloghome(index):
    return render(requests.request,'blog.html')

def blogpost(request,slug):
    return render(requests.request,'blogpost.html')