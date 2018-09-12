from pymongo import MongoClient

client = MongoClient(host='localhost',port=27017)
db = client['youdeyi']['askDocker39']
#{'全部问题': '医生，你好。不知道怎么回事最近身体特别', '回答数': '2个回答', '性别': '男', '_id': ObjectId('5b98c6c05f627d5ffa62d5e8'), '年龄': '19岁', '问题url链接': 'http://ask.39.net/question/55757041.html', '提问时间': '21分前', '疾病标签': '睡意', '科室': '中医养生', '关键字': ['心悸', '大便干燥', '疲倦乏力', '睡意', '苍白', '精神', '气短', '眼花', '血虚', '生物钟', '失眠多梦', '头晕乏力', '萎黄', '神经']}

#取出mongodb中的数据，
# 之后通过jsonpath或者正则取出相应数据写入文件中，这个文件就是用来做词云分析的
rst = db.count()


#储存数据为csv格式的文件
#
print(rst)
date = '2018-11-09'
date = date.split('-')
print(date)