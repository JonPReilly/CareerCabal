# -*- coding: utf-8 -*-
import scrapy
from django.utils.html import strip_tags

from apps.job.models import Job


class SlackSpider(scrapy.Spider):
    download_delay = 4
    name = 'Slack'
    start_urls = [
        'https://slack.com/jobs#openings',
    ]

    def parse(self, response):
        try:
            job = {
            'url': response.url,
            'title': response.css('h3.u-text--center::text').extract_first().strip(),
            'company': 'Slack',
            'location': response.css('span.career-deatil-location p::text').extract_first().strip(),
            'description': strip_tags(response.css('div[class="col-8--centered career-details-description"]').extract_first().strip()),
            'experience': '\n'.join(response.css('div[class="col-8--centered career-details-description"] li::text').extract())

            }
        except AttributeError:
            job = {}
        yield job
        for job in response.css('a.link-careers-apply::attr(href)').extract():
            job_url = job
            if job_url is not None:
                absolute_url = job_url
                if Job.objects.filter(url=response.urljoin(job_url)).exists():
                    self.logger.info("Ignoring <" + absolute_url + "> : Job with that URL already exists.")
                else:
                    self.logger.info("Scraping: <" + absolute_url + ">")
                    yield scrapy.Request(absolute_url)
