from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"Election_Portal/index.html")
def home(request):
	return render(request,"Election_Portal/home.html")