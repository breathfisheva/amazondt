# use proxy on webdriver:

from selenium import webdriver
myProxy = '85.193.229.6:42098'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % myProxy)
chrome = webdriver.Chrome(options=chrome_options)
chrome.get('https://httpbin.org/ip')