import scrapy
import telegram
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
bot = telegram.Bot(token=TOKEN)
tomorrow = datetime.date.today() + datetime.timedelta(days=1)


class BlogSpider(scrapy.Spider):
    name = 'SanSiroEventsspider'
    start_urls = ['http://www.eventiasansiro.it']

    def parse(self, response):
        for event in response.css('.rettangolo'):
            dateSplit = event.css('.dataEv::text').extract_first().split(" ")
            dateEvent = datetime.datetime.strptime(dateSplit[1].zfill(2) + dateSplit[2] + dateSplit[3].replace(",", ""),
                                                   '%d%B%Y').date()
            eve = event.css('.tipoEvento::text').extract_first()
            # dateEvent = dateEvent = datetime.datetime.strptime("22settembre2018", '%d%B%Y').date()
            scraped_info = {
                'evento': eve,
                'dataEvento': event.css('.dataEv::text').extract_first(),
                'datetime': dateEvent,
                'domani': tomorrow == dateEvent,
                'weekday': tomorrow.isoweekday(),
                'test': dateSplit[1] + " " + dateSplit[2] + " " + dateSplit[3].replace(",", "")
            }

            yield scraped_info
            
            bot.send_message(chat_id=165760372, text="Hey guys!!")

            if tomorrow == dateEvent and tomorrow.isoweekday():
                bot.send_message(chat_id=CHATID,
                                 text="Hey guys! This is a friendly reminder that tomorrow there is an event in Milano San Siro. Remember to park in the right spot!!")
                bot.send_message(chat_id=CHATID, text=eve)
