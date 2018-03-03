# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from packages.importing.JobImporter import JobImporter


class JobScrapingPipeline(object):
    jobImporter = JobImporter()

    def process_item(self, item, spider):

        self.jobImporter.addJob(item)


        return item
