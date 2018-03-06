# -*- coding: utf-8 -*-
import scrapy
from django.utils.html import strip_tags

from apps.job.models import Job


class FacebookSpider(scrapy.Spider):
    download_delay = 4
    name = 'Facebook'
    start_urls = [
        'http://www.facebook.jobs/jobs/?q=Software+Engineer&sort=date&location=United+States#7',
        'http://www.facebook.jobs/jobs/?q=&sort=date&location=United+States#',
        'http://www.facebook.jobs/jobs/?q=&sort=date#',
        'http://www.facebook.jobs/jobs/?q=Engineer&sort=date#'
    ]

    def parse(self, response):
        job = {
            'url': response.url,
            'title': response.css('span[itemprop="title"]::text').extract_first(),
            'company': response.css('span[itemprop="name"]::text').extract_first(),
            'location': response.css('span[itemprop="addressLocality"]::text').extract_first() + ", " + response.css(
                'span[itemprop="addressRegion"]::text').extract_first(),
            'description': strip_tags(response.css('div[itemprop="description"]').extract_first()),
            'experience': strip_tags(response.css('div[itemprop="description"]').css('li').extract())
        }
        yield job
        for job in response.css('li.direct_joblisting'):
            job_url = job.css("a::attr(href)").extract_first()
            if job_url is not None:
                absolute_url = response.urljoin(job_url)
                if Job.objects.filter(url=response.urljoin(job_url)).exists():
                    self.logger.info("Ignoring <" + absolute_url + "> : Job with that URL already exists.")
                else:
                    self.logger.info("Scraping: <" + absolute_url + ">")
                    yield scrapy.Request(absolute_url)
