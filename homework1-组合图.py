# -*- coding: utf-8 -*-
"""
Created on 20230404

@author: Sherry
"""

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker


def bar_datazoom_slider() -> Bar:
    c = (
        Bar()
        .add_xaxis(Faker.days_attrs)
        .add_yaxis("喜茶", Faker.days_values)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="23年3月喜茶销量柱状图（slider-水平）"),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c


def line_markpoint() -> Line:
    c = (
        Line()
        .add_xaxis(["葡萄味","草莓味","香蕉味","橘子味","苹果味","巧克力","原味"])
        #.add_xaxis(Faker.choose())
        .add_yaxis(
            "喜茶",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
        )
        .add_yaxis(
            "奈雪的茶",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="喜茶-奈雪口味销量折线图"))
    )
    return c


def pie_rosetype() -> Pie:
    v = ["北京","上海","深圳","广州","成都","厦门","香港"]
    c = (
        Pie()
        #.add(
        #    "",
        #    [list(z) for z in zip(v, Faker.values())],
        #    radius=["30%", "75%"],
        #    center=["50%", "50%"],
        #    rosetype="radius",
        #    label_opts=opts.LabelOpts(is_show=False),
        #)
        .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["50%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="喜茶地区销售玫瑰图"))
    )
    return c


def grid_mutil_yaxis() -> Grid:
    x_data = ["{}月".format(i) for i in range(1, 13)]
    y_data = [122,155,200,300,340,380,300,234,210,190,130,120]
    z_data = [150,140,190,250,220,280,290,250,180,220,150,60]
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis(
            "喜茶销售额",
            y_data,
            yaxis_index=0,
            color="#d14a61",
        )
        .add_yaxis(
            "奈雪销售额",
            z_data,
            yaxis_index=1,
            color="#5793f3",
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="喜茶销售额",
                type_="value",
                min_=0,
                max_=500,
                position="right",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 万元"),
            )
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                name="喜茶声誉变化",
                min_=0,
                max_=25,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 分"),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name="奈雪销售额",
                min_=0,
                max_=500,
                position="right",
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 万元"),
            ),
            title_opts=opts.TitleOpts(title="Grid-喜茶奈雪多轴图"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )
    line = (
        Line()
        .add_xaxis(x_data)
        .add_yaxis(
            "平均温度",
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="#675bba",
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    return Grid().add(
        bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    )


def liquid_data_precision() -> Liquid:
    c = (
        Liquid()
        .add(
            "lq",
            [0.8560],
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-数据精度"))
    )
    return c


def table_base() -> Table:
    table = Table()

    headers = ["奶茶品牌", "市场规模", "品牌调性", "客单价","zxr喜欢的程度"]
    rows = [
        ["喜茶", 300, "high", 19,4],
        ["奈雪的茶",200, "high", 22,4],
        ["本宫的茶", 150, "high", 18,3],
        ["茶百道", 170, "mass", 12,4],
        ["茶话弄", 80, "niche", 15,5],
        ["快乐柠檬", 150, "medium", 15,5],
        ["乐乐茶", 190, "high", 18,5],
    ]
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="奶茶竞争格局")
    )
    return table


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)#Page内置了两种布局：simple，draggable
    page.add(
        bar_datazoom_slider(),
        line_markpoint(),
        pie_rosetype(),
        grid_mutil_yaxis(),
        liquid_data_precision(),
        table_base(),
    )
    page.render("./output/组合图.html")


if __name__ == "__main__":
    page_simple_layout()
