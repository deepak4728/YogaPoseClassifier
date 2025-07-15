from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Welcome to the Yoga Pose Classifier!")

def about(request):
    return HttpResponse("Welcome to the Yoga Pose Classifier about!")

def contact(request):
    return HttpResponse("Welcome to the Yoga Pose Classifier contact!")