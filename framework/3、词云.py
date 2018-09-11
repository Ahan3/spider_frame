import jieba
text="李小璐给王思聪买了微博热搜"
# result=jieba.cut(text)
# print("切分结果:  "+",".join(result))

# jieba.suggest_freq(('微博'),True)
# jieba.suggest_freq(('热搜'),True)
# result = jieba.cut(text)
# print(result)
# print(','.join(result))

with open("../info.csv") as f:
    text = f.read()
stopwords = {}.fromkeys(text.split('\n'))

#将制定词添加到词云中
# jieba.load_userdict('')
segs = jieba.cut(text)
mytext_list = []

for seg in segs:
    if seg not in stopwords and seg!=" " and len(seg)!=1:
        mytext_list.append(seg.replace(" ",""))
cloud_text=",".join(mytext_list)

from wordcloud import WordCloud
wc = WordCloud(
    background_color="white", #背景颜色
    max_words=200, #显示最大词数
    font_path="./font/wb.ttf",  #使用字体
    min_font_size=15,
    max_font_size=50,
    width=400  #图幅宽度
    )
wc.generate(cloud_text)
wc.to_file("pic.png")