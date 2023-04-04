"""
Date: 20230404
Author: Sherry

要点说明：
1、用jieba.pseg在分词时标注词性
2、显示所有的分词，用字典记录下人名和词性
注：jieba的常见词性代号
a，形容词；c，连词；n，名词；nr，人名；ns，地名；v，动词
"""


import jieba.posseg as pseg
from pyecharts.charts import WordCloud
from pyecharts import options as opts

txt_filename = './data/text.txt'
# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成')


#import jieba
#jieba.load_userdict('./data/userdict_pseg.txt')

words =pseg.cut(content)
print('分词完成')
#pseg.cut()函数返回的是一个“生成器”，用于生成列表
#用for循环可以从“生成器”中提取列表元素，但不能提前知道列表的长度
print(words) # 这条语句无法打印出列表的内容
# generator 当列表用 但是打印不出来

word_dict = {}
print('正在统计所有词中的非人名、地名名词词语……')

count = 0  # 用于记录已处理的名词数
for one in words:
    # 为便于处理，用w记录本次循环检查的“词”，f记录对应的“词性”
    w = one.word
    f = one.flag

    if len(w) == 1:  # 忽略单字
        continue

    if w == '总书记' or w=='书记':
        w = '习近平'

    if f == 'n' or 'nr' in f: # 如果该词的词性为n，即是一个不为地名的名词，……
        if w in word_dict.keys(): # 如果该词已经在词典中，……
            word_dict[w] = word_dict[w] + 1
        else: # 如果该词不在词典中，……
            word_dict[w] = 1

    # 打印进度
    count = count + 1
    count_quo = int(count / 1000)
    count_mod = count % 1000  # 取模，即做除法得到的余数
    if count_mod == 0:  # 每逢整千的数，打印一次进度
        print('---已处理词数（千）：' + str(count_quo))  # 打印进度信息
        # print('\r已处理词数：' + '-'*count_quo + '> '\
        #      + str(count_quo) + '千', end='')  # 自行刷新的进度条

# 循环结束点
print('文本中的非地名名词统计完成')

items_list = list(word_dict.items())

##-------生成词云---------------------------------
cloud = WordCloud() # 初始化词云对象
# 设置词云图
cloud.add('',
          items_list[0:90], #元组列表，词和词频
          shape='cardioid', # 轮廓形状：'circle','cardioid','diamond',
                           # 'triangle-forward','triangle','pentagon','star'
          #mask_image='./data/likeqiang.jpg', # 轮廓图，第一次显示可能有问题，刷新即可
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[15, 50], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="宋体"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

# 设置标题
cloud.set_global_opts(title_opts=opts.TitleOpts(title="2023政府工作报告名词图"))

# render会生成HTML文件。默认是当前目录render.html，也可以指定文件名参数
out_filename = './output/词云.html'
cloud.render(out_filename)

print('生成结果文件：' + out_filename)



"""
这里是在跟用户进行交互
items_list.sort(key=lambda x:x[1], reverse=True)
print('排序完成')
total_num = len(items_list)
print('共有' + str(total_num) + '个可能的名词。')
num = input('您想查看前多少个名词？[10]:')
print(items_list[0:int(num)])


for w in words:
    print(w.word,w.flag)
i = 0
for w in words:
    i = i + 1
    print(i, w.word, w.flag)
    if 'nr' in w.flag:  # nr代表人名
        word_dict[w.word] = w.flag
        
print('-'*20)

for name,flag in word_dict.items():
    print(name, flag)
"""