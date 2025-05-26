from django.http import HttpResponse
from django.shortcuts import render

def landing1(request):
    # Facebook Pixel can be added in the template
    return render(request, "home/landing1.html")

def landing2(request):
    return render(request, "home/landing2.html")

def home_view(request):
    return HttpResponse("<h1>Hello!</h1><p>New videos will be uploaded soon.</p>")