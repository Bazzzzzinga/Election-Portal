from django.contrib import admin
from .models import Election,Comment,Candidate,Voter,Branch
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
   inlines = [CandidateInline,VoterInline]
class CandidateAdmin(admin.ModelAdmin):
	inlines=[CommentInline]
admin.site.register(Election,ElectionAdmin)
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Comment)
admin.site.register(Voter)
admin.site.register(Branch)