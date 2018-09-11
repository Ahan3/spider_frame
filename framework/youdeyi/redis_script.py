import redis


r = redis.StrictRedis(host='localhost',port=6379,db=0)
#中医养生
r.lpush("xunyispider:strat_urls",'http://ask.39.net/news/4378-1.html')
#中医妇科
r.lpush("xunyispider:strat_urls",'http://ask.39.net/news/4376-1.html')
#中医儿科
r.lpush("xunyispider:strat_urls",'http://ask.39.net/news/4377-1.html')
#中医皮肤科
r.lpush("xunyispider:strat_urls",'http://ask.39.net/news/319465683-1.html')
