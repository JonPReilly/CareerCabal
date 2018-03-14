import scrapy

from django.utils.html import strip_tags
from scrapy.selector import Selector

from apps.job.models import Job

from job_scraping.spiders.DynamicPageSpider import DynamicPageSpider


class TwitterSpider(DynamicPageSpider):
    download_delay = 4
    name = 'Atlassian'
    start_urls = ['https://www.atlassian.com/company/careers/all-jobs']

    def scrape(self, page_content, response):
        self.selector = Selector(text=page_content)
        job_links = self.selector.css('tr.data-row a::attr(href)').extract()
        location = self.selector.css('span.job-detail::text').extract_first()
        if location is None:
            location = ""

        job = {
            'url': response.url,
            'company': 'Atlassian',
            'title': self.selector.css('h1.job-title::text').extract_first(),
            'location': location.replace(", USA", ""),
            'description': strip_tags(self.selector.css('div.wysiwyg').extract_first()),
            'experience': ''
        }

        return job_links, [job]
