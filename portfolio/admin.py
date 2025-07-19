from django.contrib import admin
from django.contrib import admin
from .models import Portfolio, Project
# Register your models here.



class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1 # Show 1 extra empty project form

class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]
    list_display = ('full_name', 'email', 'user')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Project)