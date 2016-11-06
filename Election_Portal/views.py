from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Election,Comment
# Create your views here.
@login_required
def home(request):
	list_of_elections=Election.objects.all()
	future_elections=sorted((i for i in list_of_elections if i.vote_start_time>timezone.now()),key=lambda x:x.vote_start_time)
	ongoing_elections=sorted((i for i in list_of_elections if i.vote_start_time<=timezone.now()<=i.vote_end_time),key=lambda x:x.vote_start_time)
	past_elections=sorted((i for i in list_of_elections if i.vote_end_time<timezone.now()),key=lambda x:x.vote_start_time,reverse=True)
	return render(request,"Election_Portal/home.html",{
		'upcoming_elections':future_elections,
        'ongoing_elections':ongoing_elections,
        'past_elections':past_elections,
	})
@login_required
def OnGoing(request):
	return render(request,"Election_Portal/OnGoing.html")
@login_required
def nominations(request,pk):
	try:
		election=Election.objects.get(pk=pk)
	except:
		return HttpResponseRedirect(reverse('Election_Portal:index'))
	if election.nom_start_time<=timezone.now()<=election.nom_end_time:
		return render(request,'Election_Portal/nominations.html',{
            'election':election
        })
	else:
		return HttpResponseRedirect(reverse('Election_Portal:index'))
@login_required
def status(request):
	return render(request,"Election_Portal/status.html")
@login_required
def past(request):
	return render(request,"Election_Portal/past.html")
@login_required
def ama(request,pk):
	return render(request,"Election_Portal/ama.html")
@login_required
def aboutupcoming(request):
	return render(request,"Election_Portal/aboutupcoming.html")
@login_required
def vote(request,pk):
	return render(request,"Election_Portal/OnGoing.html")