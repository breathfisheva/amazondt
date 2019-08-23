#{'85.193.229.6:42098', '176.105.100.62:3128', '200.122.209.78:55167'}

from selenium import webdriver

clothing_best_sellers = 'https://www.amazon.com/Best-Sellers/zgbs/fashion'


myProxy =  {
    "http": 'http://85.193.229.6:42098',
    "https": 'http://85.193.229.6:42098'
}


headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % myProxy)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get(clothing_best_sellers)
# pageSource = driver.page_source


import requests
from lxml.html import fromstring

response = requests.get(clothing_best_sellers, proxies=myProxy, headers=headers)
content = fromstring(response.text)
print(content)


