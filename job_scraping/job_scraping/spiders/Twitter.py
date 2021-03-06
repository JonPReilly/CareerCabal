import scrapy
from django.utils.html import strip_tags

from apps.job.models import Job


class TwitterSpider(scrapy.Spider):
    download_delay = 4
    name = 'Twitter'
    start_urls = [
                     'https://careers.twitter.com/content/careers-twitter/en/jobs-search.html?q=software&start=' + str(
                         (start * 10)) for start in range(3)
                 ] + [
                     'https://careers.twitter.com/content/careers-twitter/en/jobs-search.html?start=' + str(
                         (start * 10))
                     for start in range(2)
                 ]

    def parse(self, response):
        if response.url not in self.start_urls:
            job = {
                'url': response.url,
                'company': 'Twitter',
                'title': response.css('title::text').extract_first(),
                'location': response.css('div.parbase::text')[1].extract().strip(),
                'description': strip_tags(response.css('div.parbase')[2].extract()),
                'experience': strip_tags(response.css('div.parbase')[2].css('ul')[0:1].css('li').extract())
            }
            yield job
        for job in response.css('li.job-search-item'):
            job_url = job.css('a::attr(href)').extract_first()
            if job_url is not None:
                absolute_url = response.urljoin(job_url)
                if Job.objects.filter(url=response.urljoin(job_url)).exists():
                    self.logger.info("Ignoring <" + absolute_url + "> : Job with that URL already exists.")
                else:
                    self.logger.info("Scraping: <" + absolute_url + ">")
                    yield scrapy.Request(absolute_url)
