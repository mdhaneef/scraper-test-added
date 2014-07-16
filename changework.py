"""This file is a Changeworknow spider created on top of the ATSSpider
scrapy crawl changeworknow url="http://isw.changeworknow.co.uk/dixons_retail/vms/e/vacancies/search/new"

sample url:
    http://isw.changeworknow.co.uk/wagamama/vms/e/wagamama/search/new
    http://isw.changeworknow.co.uk/gordonramsay/vms/e/gordonramsay/search/new
"""
import re
import urllib
import json

from urlparse import urljoin, urlparse
from datetime import datetime

from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from brightcorp.base.atsspiders import ATSSpider
from brightcorp.items import BrightcorpItemLoader

class Changeworknow(ATSSpider):

    name = 'changeworknow'
    allowed_domains = ["search.jobvite.com"]
    start_urls = [
                "http://search.jobvite.com/api/jobsearch?limit=10000&start=0&facet=true&fname=companyId&fvalue=qz29Vfwp"
                ]

    def parse(self, response):
        ## parse initial page
          pass


    def parse_page(self, response):

        ## parse jobs listings page
        final_result = []

       jsonresponse = json.loads(response.body_as_unicode())


       for it in jsonresponse['response']:
                item = BitcorpItem()
                item['jobtitle'] = it['jobtitle']
                item['formattedLocation'] = it['formattedLocation']
                item['jobId'] = it['jobId']
                item['company'] = it['company']
                item['companyLogo'] = it['companyLogo']
                item['companyId'] = it['companyId']
                item['careerSite'] = it['careerSite']
                item['url'] = it['url']
                final_result.append(item)
                                                   return final_result
        pass

    def parse_job(self, response):
        ## parse each job page
          final_page = []
       for sel in response.xpath('//ul/li'):
            item =BitcorpItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            final_page.append(item)
       for p in divs.xpath('.//p'):
                item=BitcorpItem()
                item['data'] = p.extract()
                final_page.apend(item)

      return final_page
        pass
