from django.shortcuts import render
from django.http import HttpResponse
from instructors.models import Instructor

# Create your views here.

def hello(request):
    print (request)
    print (request.method)
    print (request.path)
    print (request.GET)
    print (request.POST)
    return render (request, "index.html")

def instructors_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructors.html", {"instructor":instructors})

def for_post(request):
    print (request)
    print (request.method)
    print (request.path)
    print (request.GET)
    print (request.POST['text'])
    return render (request, "for_post.html")

def contacts(request):
    return render (request, "contact.html")
