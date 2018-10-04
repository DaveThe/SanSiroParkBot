# -*- coding: utf-8 -*-
import scrapy
import telegram
import datetime
import dateparser
from scrapy import Request

# import locale


# locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
# bot = telegram.Bot(token='')
tomorrow = datetime.date.today() + datetime.timedelta(days=1)


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['eventiasansiro.it']
    start_urls = ['http://www.eventiasansiro.it/']
    token = ''
    chatid = ''

    def parse(self, response):
        # print("Existing settings: %s" % self.settings.attributes.keys())
        # print("Existing settings: %s" % self.settings.attributes['token'])
        # print("Existing settings: %s" % self.settings.attributes['chatid'])
        bot = telegram.Bot(token=self.token)
        # self.token =
        for event in response.css('.rettangolo'):
            dateSplit = event.css('.dataEv::text').extract_first().split(" ")
            # dateEvent = datetime.datetime.strptime(dateSplit[1].zfill(2) + dateSplit[2] + dateSplit[3].replace(",", ""),'%d%B%Y').date()
            dateEvent = dateparser.parse(dateSplit[1].zfill(2) + dateSplit[2] + dateSplit[3].replace(",", ""))
            eve = event.css('.tipoEvento::text').extract_first()
            # dateEvent = dateEvent = datetime.datetime.strptime("22settembre2018", '%d%B%Y').date()
            scraped_info = {
                'token': self.token,
                'chatid': self.chatid,
                'evento': eve,
                'dataEvento': event.css('.dataEv::text').extract_first(),
                'datetime': dateEvent,
                'Tomorrow': tomorrow,
                'isTomorrow': tomorrow == dateEvent,
                'weekday': tomorrow.isoweekday(),
                'test': dateSplit[1] + " " + dateSplit[2] + " " + dateSplit[3].replace(",", "")
            }

            yield scraped_info

            #bot.send_message(chat_id=165760372, text="Hey guys!!")

            if tomorrow == dateEvent and tomorrow.isoweekday():
                bot.send_message(chat_id=self.chatid,
                                 text="Hey guys! This is a friendly reminder that tomorrow there is an event in Milano San Siro. Remember to park in the right spot!!")
                bot.send_message(chat_id=self.chatid, text=eve)
