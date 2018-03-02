from datetime import datetime, timedelta
from django.db import models

from cities.models import City
from apps.company.models import Company


class Job(models.Model):
    DEFAULT_DAYS_VALID = 30

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    experience = models.TextField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    url = models.URLField(unique=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.company) + ": " + str(self.title)
