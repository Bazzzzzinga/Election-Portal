from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
class Election(models.Model):
    election_name=models.CharField(max_length=50)
    nom_start_time=models.DateTimeField('Nominations start time')
    nom_end_time=models.DateTimeField('Nominations end time')
    vote_start_time=models.DateTimeField('Voting start time')
    vote_end_time=models.DateTimeField('Voting end time')
    desc=models.TextField()
    def __str__(self):
        return self.election_name
    def nomval(self):
    	if self.nom_start_time>timezone.now():
    		return "1"
    	elif self.nom_end_time>=timezone.now():
    		return "2"
    	else:
    		return "3"
class Branch(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class Comment(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    comment_content=models.CharField(max_length=3000)
    comment_time=models.DateTimeField('Comment Time')
    isCandidate=models.BooleanField(default=False)
    def __str__(self):
        return self.comment_content
class Candidate(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    work_experience=models.TextField()
    user=models.CharField(max_length=30,primary_key=True)
    vote_count=models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Voter(models.Model):
    election=models.ForeignKey(Election,on_delete=models.CASCADE)
    user=models.CharField(max_length=30,primary_key=True)