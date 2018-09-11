import requests

url ='http://ask.39.net/news/4378-1.html'

rst = requests.get(url)
print(rst.status_code)