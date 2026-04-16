from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'index_number', 'is_active')
    list_editable = ('index_number', 'is_active')