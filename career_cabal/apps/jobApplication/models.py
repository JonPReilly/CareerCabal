from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.formats import date_format

from apps.job.models import Job


class JobApplication(models.Model):
    STATUSES = (
        (0, 'Accepted'),
        (1, 'Applied'),
        (2, 'Coding Challange'),
        (3, 'Grave Yard'),
        (4, 'Not Interested'),
        (5, 'Offer'),
        (6, 'Onsite Inteview'),
        (7, 'Phone Interview'),
        (8, 'Saved')
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=1000, blank=True)
    status = models.IntegerField(choices=STATUSES, default=1)

    def getHistory(self):
        return ApplicationHistory.objects.filter(application=self).order_by('timeStamp')

    def save(self, *args, **kwargs):
        super(JobApplication, self).save(*args, **kwargs)
        new_status, created = ApplicationHistory.objects.get_or_create(application=self, status=self.status)
        if (not created):
            new_status.save()

    def __str__(self):
        return "{0}\t: [{1}]\t ({2}) - {3}".format(self.user, self.job, self.status,
                                                   date_format(self.date_applied, format='SHORT_DATETIME_FORMAT'))


class ApplicationHistory(models.Model):
    application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=JobApplication.STATUSES, default=1)

    def save(self, *args, **kwargs):
        self.status = self.application.status
        super(ApplicationHistory, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} - {1} ({2}) at {3}".format(self.application.user, self.application.job, self.status,
                                               date_format(self.time_stamp, format='SHORT_DATETIME_FORMAT'))
