# -*- coding: utf-8 -*-
"""
Created on Tue Apr 4 2023
@author: Sherry
"""
'''
Map 中国地图 背景是全国各个省份的喜茶门店数量，数据为虚构
'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 注： map.add()函数中的maptype参数指明地图类型
# 具体参考 pyecharts.datasets.map_filenames.json 文件

src_filename = './data/xicha1.csv'

src_file = open(src_filename,encoding='gbk')
line_list = src_file.readlines()
src_file.close()
print(line_list)

area_list = []
cnt_list = []

del line_list[0] #删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    area_cnt = line.split(',')
    area_list.append(area_cnt[0])
    cnt_list.append(int(area_cnt[1]))

print(area_list)
print(cnt_list)

## 用于绘图的数据，由上面的列表生成元组：
area_cnt_tuple = list(zip(area_list,cnt_list))

print(area_cnt_tuple)

##prov_list = [('广东省', 98), ('北京市', 125), ('上海市', 134),
           ##  ('江西省', 56), ('湖南省', 136), ('浙江省', 139),
           ##  ('江苏省', 88)]

## 在中国地图上绘制上述数据，即填充对应省份的区域
c = (
    Map()
    .add("喜茶",
         area_cnt_tuple,
         #prov_list,
         maptype="china",
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国地图-喜茶分布（渐变型）"),
        visualmap_opts=opts.VisualMapOpts(max_=200),  # 此项配置渐变色的最大数值
    )
)

c.render('./output/中国地图.html')