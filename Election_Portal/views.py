from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,"Election_Portal/index.html")
def home(request):
	return render(request,"Election_Portal/home.html")
def OnGoing(request):
	return render(request,"Election_Portal/OnGoing.html")
def nominations(request):
	return render(request,"Election_Portal/nominations.html")
def status(request):
	return render(request,"Election_Portal/status.html")
def past(request):
	return render(request,"Election_Portal/past.html")
def ama(request):
	return render(request,"Election_Portal/ama.html")
def login(request):
	return render(request,"Election_Portal/login.html")
def aboutupcoming(request):
	return render(request,"Election_Portal/aboutupcoming.html")
def altlogin(request):
	return render(request,"Election_Portal/alternate_login.html")
