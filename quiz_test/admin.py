from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Quiz_Question)
class Quiz_QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish',   
                       'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish') 


admin.site.register(Answer_Options)
admin.site.register(Quiz)
admin.site.register(Topic)
admin.site.register(Sub_Topic)

