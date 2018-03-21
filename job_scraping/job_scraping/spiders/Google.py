import scrapy
import time

from django.utils.html import strip_tags
from scrapy.selector import Selector

from apps.job.models import Job

from job_scraping.spiders.DynamicPageSpider import DynamicPageSpider


class GoogleSpider(DynamicPageSpider):
    download_delay = 20
    name = 'Google'
    start_urls = [
        'https://careers.google.com/jobs',

    ]
    base_url = "https://careers.google.com/jobs"
    initial = True

    def scrape(self, page_content, response):
        self.selector = Selector(text=page_content)
        job_links = self.selector.css('a[class="sr-title text"]::attr(href)').extract()
        job_links = [self.base_url + link for link in job_links]
        location = self.selector.css('a[class="details-location body1 secondary-text"]::text').extract_first()
        if location is None:
            location = ""
        job = {
            'url': response.url,
            'company': self.selector.css('div.company-name-panel span::text').extract_first(),
            'title': self.selector.css('a[class="title text"]::text').extract_first(),
            'location': location.replace(", United States", ""),
            'description': strip_tags(
                self.selector.css('div[class="description-section text with-benefits"]').extract_first()),
            'experience': strip_tags(
                self.selector.css('div[class="description-content text stacked-requirements"]').extract_first())
        }

        return job_links, [job]

    def preparePage(self):
        if self.initial:
            self.driver.find_elements_by_css_selector('span[class="GXRRIBB-Q-m no-wrap"]')[2].click()
            self.driver.find_element_by_xpath('//button[.//span[text()="Sort date"]]').click()
            self.driver.find_element(value="gjlftb").click()
            self.driver.find_element(value="gjlftb").clear()
            self.driver.find_element(value="gjlftb").send_keys("United States")
            time.sleep(1)
            self.driver.find_element(value="gjlftb").send_keys("\n")
            time.sleep(1)
            self.driver.find_element(value="search-text-box").send_keys("engineer\n")
            self.waitForJavascriptToLoad()
        self.initial = False
