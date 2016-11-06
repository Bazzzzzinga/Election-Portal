from django.contrib import admin
from .models import Election,Comment
# Register your models here.
class CommentInline(admin.StackedInline):
    model=Comment
    extra=0
class ElectionAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
admin.site.register(Election,ElectionAdmin)
admin.site.register(Comment)