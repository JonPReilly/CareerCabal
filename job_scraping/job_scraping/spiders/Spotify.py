import scrapy
import time

from django.utils.html import strip_tags
from scrapy.selector import Selector

from apps.job.models import Job

from job_scraping.spiders.DynamicPageSpider import DynamicPageSpider


class SpotifyScraper(DynamicPageSpider):
    download_delay = 20
    name = 'Spotify'
    start_urls = [
        'https://www.spotifyjobs.com/search-jobs/',

    ]

    custom_settings = {
        'DEPTH_LIMIT': 3,
    }

    def __init__(self, search_query='', *args, **kwargs):
        self.search_query = search_query
        super(SpotifyScraper, self).__init__(*args, **kwargs)

    def scrape(self, page_content, response):
        self.selector = Selector(text=page_content)
        job_links = self.selector.css('a[class="table-item--link"]::attr(href)').extract()
        try:
            location = self.selector.css('div[class="single-post--meta"] a::text').extract()[-2]
        except IndexError:
            location = ""
        if location is None:
            location = ""
        job = {
            'url': response.url,
            'company': 'Spotify',
            'title': self.selector.css('h1::text').extract_first(),
            'location': location,
            'description': strip_tags(
                self.selector.css('div[class="column-inner"]').extract_first()).strip(),
            'experience': strip_tags(
                self.selector.css('div[class="column-inner"] ul').extract()[-1]).strip() if self.selector.css('div[class="column-inner"] ul') else None
        }

        return job_links, [job]

    def preparePage(self):
        pass
