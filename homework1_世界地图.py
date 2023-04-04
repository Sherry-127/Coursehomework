

"""
Date:
Author: Sherry
世界地图作业

要点说明：
Map 地图
在世界地图上填充区域色块

参考pyecharts 官方文档
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 注： map.add()函数中的maptype参数指明地图类型
# 具体参考 pyecharts.datasets.map_filenames.json 文件



src_filename = './data/xicha2.csv'

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

# 如果不是Faker生成而是自己来定义一个list的话，那么就先定义一个list，然后再函数里直接完成即可

c = (
    Map()
    .add("喜茶",
         #[list(z) for z in zip(Faker.country, Faker.values())],
         area_cnt_tuple,
         maptype="world",
         is_map_symbol_show=False,  # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界地图-喜茶分布"),
        visualmap_opts=opts.VisualMapOpts(max_=400, is_piecewise=True),
    )
)

c.render('./output/世界地图.html')
