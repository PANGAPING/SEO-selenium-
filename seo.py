import urllib.request
import urllib
import urllib.error
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import *
import time
import math
import random
import threading

class SEO():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_thread = 40 
        self.start_point = "https://www.baidu.com/link?url=jHdCXYkc_XM3Q9v-bmed9ZoY2JLMy2zWWQuC446XE3zMQosgQ9twMWHKW10Imjwf&wd=&eqid=ee5823cd00065bd5000000065e244e4c"
        self.proxies = []
        self.current_proxy_index = 0
        self.url_list = []
        self.headers = []

    
    #获取代理地址，我这里使用的是大象代理   
    def get_proxies(self):
        proxy_warehouse = "http://tpv.daxiangdaili.com/ip/?tid=556093805368070&num="+str(self.max_thread)+"&delay=3&category=2&protocol=https&sortby=speed"
        body = urllib.request.urlopen(proxy_warehouse).read().decode('utf-8')
        proxies = body.split("\r\n")
        return proxies

    
    def start(self):
        self.proxies = self.get_proxies();
        
        self.current_proxy_index = self.max_thread;
        for i in range(self.max_thread):
            proxy = self.proxies[i]
            th = threading.Thread(target=self.startASpider,args=(proxy,))
            th.start()


    def startASpider(self,proxy):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--user-agent="'+self.headers[random.randint(0,len(self.headers))]+'"')
        chrome_options.add_argument("-proxy-server=http://" + proxy)
        capabilities = webdriver.DesiredCapabilities.CHROME

        #使用谷歌浏览器驱动，驱动自行搜索chromedriver下载与谷歌浏览器相适应的版本
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:\\Users\\WaveDeng\\Desktop\\chromedriver.exe",desired_capabilities=capabilities)

        driver.implicitly_wait(10)
        driver.get(self.start_point)
        while(True):
            try:
                time.sleep(random.randint(6,20))
                driver.get(self.url_list[random.randint(0,len(self.url_list)-1)])

                
                if(random.random()<0.1):
                    raise RuntimeError
           #若有异常就换个代理重新访问 
            except:
                proxy = self.proxies[self.current_proxy_index]
                self.current_proxy_index += 1
                if(self.current_proxy_index >= len(self.proxies)):
                    self.current_proxy_index = 0;
                    self.proxies = self.get_proxies();
                driver.close()
                self.startASpider(proxy)
                break

#你需要访问的地址
urls = ["https://www.wavedeng.com/blog",
    "https://www.wavedeng.com/Blog/Passage?id=4",
    "https://www.wavedeng.com/Blog/Passage?id=3",
    "https://www.wavedeng.com/about",
    "https://www.wavedeng.com/"]

#在网上搜集到的浏览器头
headers = ["Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
           "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
           "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
           "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
           "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
           "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
    ]

seo = SEO()
seo.max_thread = 40
seo.url_list = urls
seo.headers = headers
seo.start()








