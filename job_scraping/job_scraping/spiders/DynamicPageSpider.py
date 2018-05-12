import scrapy
import time

from selenium import webdriver

from apps.job.models import Job


class DynamicPageSpider(scrapy.Spider):
    name = "Abstract"
    download_delay = 7
    WAIT_JS_LOAD_SECONDS = 7
    start_urls = []
    selector = None

    def __init__(self):

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome('./../../webdrivers/chromedriver', options=self.options)

    def parse(self, response):
        self.driver.get(response.url)
        self.waitForJavascriptToLoad()
        self.preparePage()
        page_content = self.pullContentFromPage()
        job_urls, jobs = self.scrape(page_content, response)

        for job in jobs:
            yield job

        for url in job_urls:
            if Job.objects.filter(url=url).exists():
                self.logger.info("Ignoring <" + url + "> : Job with that URL already exists.")
            else:
                self.logger.info("Scraping: <" + url + ">")
                yield scrapy.Request(url)

    def pullContentFromPage(self):
        page_content = self.driver.execute_script("return document.documentElement.innerHTML;")
        return page_content

    def waitForJavascriptToLoad(self):
        time.sleep(self.WAIT_JS_LOAD_SECONDS)

    def scrape(self, page_content, response):
        self.driver.close()
        raise NotImplemented

    def preparePage(self):
        pass
