from django.contrib import admin
from .models import Election,Comment,Candidate,Voter,Branch
# Register your models here.
class CommentInline(admin.StackedInline):
    model=Comment
    extra=0
class CandidateInline(admin.StackedInline):
    model=Candidate
    extra=0
class VoterInline(admin.StackedInline):
    model=Voter
    extra=0

class ElectionAdmin(admin.ModelAdmin):
    inlines = [CommentInline,CandidateInline,VoterInline]
admin.site.register(Election,ElectionAdmin)
admin.site.register(Comment)
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Branch)