from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    search_fields = ['company__name', 'title']

    class Meta:
        model = Job


admin.site.register(Job, JobAdmin)
