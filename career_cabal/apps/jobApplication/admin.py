from django.contrib import admin

from .models import JobApplication, ApplicationHistory


class ApplicationAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'job__title', 'job__company__name']

    class Meta:
        model = JobApplication


class ApplicationHistoryAdmin(admin.ModelAdmin):
    class Meta:
        model = ApplicationHistory


admin.site.register(JobApplication, ApplicationAdmin)
admin.site.register(ApplicationHistory, ApplicationHistoryAdmin)