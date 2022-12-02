from django.contrib import admin
from .models import *

admin.site.site_header = 'My Todo'

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'is_finished', 'created_date', 'due_date', 'due_time')

# Register your models here.
admin.site.register(Todo, TodoAdmin)
