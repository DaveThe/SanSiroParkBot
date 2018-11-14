# SanSiroParkBot

## Get Started
 - create an account on https://app.scrapinghub.com
 - link your github project in Code & Deploys
 - use the API to call your new sprider https://doc.scrapinghub.com/scrapy-cloud.html
    - curl -u APIKEY: https://app.scrapinghub.com/api/run.json -d project=PROJECT -d spider=SPIDER
      - if you use any parameters setted in scrapinghub you can add them like this: -d param='123124134' -d param2=12314
      
## Edit spider
 If you want to edit this spider fork it and edit the file "myspider.py" in SanSiroParkBot/SanSiroParkBot/spiders/
