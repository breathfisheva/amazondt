'''
pick up IPs automatically from https://free-proxy-list.net/
'''

import requests
from lxml.html import fromstring
from itertools import cycle

PROXY_WEBURL = "https://free-proxy-list.net/"

def get_proxies(url):
    proxies = set()

    response = requests.get(url)
    parser = fromstring(response.text)

    for i in parser.xpath("//tbody/tr")[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    return proxies



'''
# Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
# We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
'''

def rotate_ips(proxies):
    useful_proxies = set()

    proxy_pool = cycle(proxies)
    url = 'https://httpbin.org/ip'

    for i in range(1, 11):
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy})
            useful_proxies.add(proxy)
            print(response.json())
        except:
            print("Skipping. Connnection error")

    return useful_proxies


proxies = get_proxies(PROXY_WEBURL)
useful_proxies = rotate_ips(proxies)

# {'85.193.229.6:42098', '176.105.100.62:3128', '200.122.209.78:55167'}