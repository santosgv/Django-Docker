from django.shortcuts import HttpResponse, render

def home():
    return HttpResponse('home')
