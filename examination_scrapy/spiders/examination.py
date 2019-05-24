# -*- coding: utf-8 -*-
import scrapy
import json
from examination_scrapy.items import Examination

class ExaminationSpider(scrapy.Spider):
    name = "examination"
    allowed_domains = ["gkcx.eol.cn"]
    start_urls = (
        "https://gkcx.eol.cn/static/assets/json/info.json",
    )

    def parse(self, response):
       data = json.loads(response.body)
       return data