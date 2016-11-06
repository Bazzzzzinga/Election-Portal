from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
class Election(models.Model):
    election_name=models.CharField(max_length=50)
    nom_start_time=models.DateTimeField('Nominations start time')
    nom_end_time=models.DateTimeField('Nominations end time')
    vote_start_time=models.DateTimeField('Voting start time')
    vote_end_time=models.DateTimeField('Voting end time')
    candidateList=models.CharField(max_length=500,default="")
    def __str__(self):
        return self.election_name
    def listify(self):
    	return self.candidateList.split(';')[1:]
    def addToList(self,toAdd):
    	self.candidateList+=";"+toAdd;
    def nomval(self):
    	if self.nom_start_time>timezone.now():
    		return "1"
    	elif self.nom_end_time>=timezone.now():
    		return "2"
    	else:
    		return "3"
class Comment(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    comment_content=models.CharField(max_length=3000)
    comment_time=models.DateTimeField('Comment Time')
    isCandidate=models.BooleanField(default=False)
    def __str__(self):
        return self.comment_content