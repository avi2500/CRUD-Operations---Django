from django.contrib import admin
from .models import *

@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task',)
    search_fields = ('task',)
