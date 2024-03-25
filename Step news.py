from pathlib import Path
import scrapy
from datetime import datetime
import pandas as pd
import time
import re
import string

## Step News

class StepNewsSpider(scrapy.Spider):
    name = "stepnews"
    
    # try:
    #     idd= createSQLfunctions.get_id("time")+1
    # except:
    #     idd=0

    start_urls = [ 'https://stepagency-sy.net/?s=%D9%85%D8%B5%D8%B1' ]
    
    

    def parse(self, response):
        ## urls=response.xpath('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//div//a/@href').getall()
        urls=response.css("#posts-container > li > div > h3 > a::attr(href)").getall()
              
        ## print(type(urls2),'/////////////////////////////////')
        for u in urls:  
            yield scrapy.Request(u,callback=self.parse_new)
    
    def parse_new(self, response):

      link=response.url

      title=response.css('#the-post > header > div > h1::text').get()

      try:
        text1 = response.css('#the-post > div.entry-content.entry.clearfix > h2::text').getall() 
      except:
         text1 = [" "]

      text2 = response.css('#the-post > div.entry-content.entry.clearfix > p > span::text').getall()
      text = text1 + text2

      date=response.css('#the-post > header > div > div > span::text').get()  

      date=date.split(" ")
      month =date[1]
      month = month[:-1] 

      params = {"يناير":"01", "فبراير":"02", "مارس":"03", "أبريل":"04","مايو":"05", "يونيو":"06", "يوليو":"07", "أغسطس":"08","سبتمبر":"09", "اكتوبر":"10", "نوفمبر":"11", "ديسمبر":"12"}
      month=params[month]  
      date=date[2]+"/"+month+"/"+date[0]+" "+'00'+":"+'00'+":"+'00'
        # # scrapped_date=scraped_year+"/"+scraped_month+"/"+scraped_day+" "+scraped_hour+":"+scraped_min+":"+"00"
      
      datetime_object1 = datetime.strptime(date, '%Y/%m/%d %H:%M:%S' )
        

      print(title)  
      print(link)
      print(text)
      print(datetime_object1)
      print('////////////'*4)
