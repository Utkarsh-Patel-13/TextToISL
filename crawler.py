
import scrapy
from pytube import YouTube

import os
from os.path import join, isfile

class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://indiansignlanguage.org/']

    def __init__(self):
        self.file_list = [f for f in os.listdir(join('videos', 'dataset')) if isfile(join('videos', 'dataset', f))]

    def parse(self, response):
        try:
            for i in response.xpath('//*[@id="inner-slider"]'):
                
                try:
                    # cnt = 0
                    # nm_cnt = 0
                    # left = 0
                    # print(f'\n\n\nFile list = {len(self.file_list)}\n\n\n')
                    for j in i.xpath('div/ul/li'):
                        link = j.xpath('a/@href').extract()[0]
                        text = j.xpath('a/text()').get().strip()
                        name = text.__str__() + ".mp4"

                        if len(text.split()) > 1:
                            continue

                        
                        isThere = False
                        for f in self.file_list:
                            if name.lower() == f.lower():
                                # nm_cnt += 1
                                isThere = True
                                break

                        if isThere:
                            continue

                        # if name in self.file_list:
                        #     nm_cnt += 1
                        #     # print(f'File {name} exists')
                        #     # self.file_list.remove(name)
                        #     continue
                        
                        # left += 1
                        # cnt += 1

                        if link:
                            url = link
                            yield scrapy.Request(url, self.get_ytlink)

                    # print(f'\n\nnm_cnt = {nm_cnt}\n\n')
                    # print(f'\n\nleft = {left}\n\n')
                except Exception as e:
                    continue

            # print(f'\n\n\n{cnt}\n\n\n')
            # q = input("input")
        
            
        except Exception as e:
            print(str(e))

        
    def get_ytlink(self, response):
        try:

            for i in response.xpath('/html/body/div/div[3]/div/div/div[1]/main/article/div/div/div'):
                try:
                    ytlink = i.xpath('iframe/@src').extract()[0]

                    yt = YouTube(ytlink)

                    filters = yt.streams.filter(progressive=True, file_extension='mp4')

                    filters.get_lowest_resolution().download(output_path=join('videos', 'dataset'), skip_existing=True)
                except Exception as e:
                    continue
        except Exception as e:
            print(str(e))