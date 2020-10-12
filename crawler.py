
import scrapy
from pytube import YouTube

class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://indiansignlanguage.org/']

    def parse(self, response):
        try:
            cnt = 0
            # for i in response.xpath('/html/body/div/div[2]/div/div/div/main/article/div/div/div[3]/div[2]/div/div[2]/div/div[1]/ul/li'):
            for i in response.xpath('//*[@id="inner-slider"]'):
                
                try:
                    for j in i.xpath('div/ul/li'):
                        link = j.xpath('a/@href').extract()[0]
                        text = j.xpath('a/text()').get()
                        if len(text.split()) > 1:
                            continue
                        cnt += 1
                        
                        if link:
                            url = link
                            yield scrapy.Request(url, self.get_ytlink)
                        if cnt > 10:
                            break
                except Exception as e:
                    continue
            print(cnt)
        except Exception as e:
            print(str(e))

    def get_ytlink(self, response):
        try:

            for i in response.xpath('/html/body/div/div[3]/div/div/div[1]/main/article/div/div/div'):
                try:
                    ytlink = i.xpath('iframe/@src').extract()[0]

                    yt = YouTube(ytlink)

                    filters = yt.streams.filter(progressive=True, file_extension='mp4')

                    filters.get_lowest_resolution().download(output_path='videos/')
                except Exception as e:
                    continue
        except Exception as e:
            print(str(e))