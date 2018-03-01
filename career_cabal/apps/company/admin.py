from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']

    class Meta:
        model = Company

admin.site.register(Company, CompanyAdmin)