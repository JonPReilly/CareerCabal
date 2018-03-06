import scrapy
from django.utils.html import strip_tags

from apps.job.models import Job


class BuiltInBoston(scrapy.Spider):
    download_delay = 4
    name = 'BuiltInBoston'
    start_urls = [
        'https://www.builtinboston.com/jobs?page=' + str(page) for page in range(3)
    ]

    def parse(self, response):
        if response.url not in self.start_urls:
            job = {
                'url': response.url,
                'company': strip_tags(response.css('div.field__item a').extract_first()).strip(),
                'title': response.css('h1.node-title span::text').extract_first().strip(),
                'location': response.css('span.company-address::text').extract_first() + " , MA",
                'description': strip_tags(response.css('div.field--name-body').extract_first()),
                'experience': ''
            }
            self.logger.info(job)
            yield job
        for job in response.css('div.wrap-view-page'):
            job_url = job.css('a::attr(href)').extract_first()
            if job_url is not None:
                absolute_url = response.urljoin(job_url)
                if Job.objects.filter(url=response.urljoin(job_url)).exists():
                    self.logger.info("Ignoring <" + absolute_url + "> : Job with that URL already exists.")
                else:
                    self.logger.info("Scraping: <" + absolute_url + ">")
                    yield scrapy.Request(absolute_url)
