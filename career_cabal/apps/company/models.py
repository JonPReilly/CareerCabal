from django.db import models

class Company(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def save(self, *args ,**kwargs):
        self.name = self.name.title()
        super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
