# from fake_useragent import UserAgent
#
# ua = UserAgent(verify_ssl=False)
#
# for i in range(100):
#     print(type(ua.random))
import json

url = 'http://ask.39.net/news/4376-1.html'

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(url)
# import requests
# proxies = {'http':'118.190.95.35:9001'}
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
# }
#
# url1 = 'https://www.baidu.com'
# url3 = 'http://httpbin.org/'
# rst = requests.get(url,headers=headers,proxies=proxies)
# print(rst.status_code)
# print(rst.text)
import redis
conn = redis.StrictRedis(host='127.0.0.1', port=6379,db=3)

rst = conn.srandmember('ip_pool').decode()
ip = eval(rst)

import requests
url = 'http://ask.39.net/news/4378-1.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
proxies = ip
# print(proxies)
try:
    rst = requests.get(url,headers=headers,proxies=proxies,timeout=2)
    print(rst.text)
except:
    conn.srem('ip_pool',proxies)
    print('删除{}'.format(proxies))