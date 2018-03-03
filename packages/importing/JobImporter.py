from apps.job.models import Job
from apps.company.models import Company
from packages.searching.LocationFinder import LocationFinder


class JobImporter:
    locationFinder = LocationFinder()

    def addJob(self, item):
        url = item['url']
        company_name = item['company']
        description = item['description']
        experience = item['experience']
        title = item['title']
        location_query = item['location']

        company, created = Company.objects.get_or_create(name=company_name)
        location = self.locationFinder.findCity(location_query)

        Job.objects.create(
            url=url,
            company=company,
            description=description,
            title=title,
            experience=experience,
            city=location
        )
