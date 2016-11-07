from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Election,Comment,Candidate,Voter,Branch
from django.db import transaction
# Create your views here.
def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days*3600*24+hours*3600+minutes*60+seconds

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
            'election':election,
            'branches':Branch.objects.all()
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
    election=get_object_or_404(Election,pk=pk)
    return render(request,"Election_Portal/OnGoing.html",{
            'time_left':convert_timedelta(election.vote_end_time-timezone.now()),
            'election':election,
            'candidates':election.candidate_set.all()
        })
def nomination_filled(request,pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('Election_Portal:index'))
    election=get_object_or_404(Election,pk=pk)
    if election.nomval()!="2":
        return HttpResponseRedirect(reverse('Election_Portal:index'))
    else:
        candidate=Candidate(name=request.POST['name'],branch=request.POST['branch'],user=request.user.username,
            work_experience=request.POST['work'],election=election)
        candidate.save()
        return HttpResponseRedirect(reverse('Election_Portal:index'))
@transaction.atomic
def vote_done(request,pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('Election_Portal:index'))
    election=get_object_or_404(Election,pk=pk)
    if Voter.objects.filter(election=election,user=request.user.username).exists():
        return HttpResponseRedirect(reverse('Election_Portal:index'))
    else:
        voter=Voter(election=election,user=request.user.username)
        voter.save()
        candidate_voted=Candidate.objects.select_for_update().filter(user=request.POST['candidate'],election=election)[0]
        candidate_voted.vote_count+=1
        candidate_voted.save()
        return HttpResponseRedirect(reverse('Election_Portal:index'))