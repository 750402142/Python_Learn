import pandas as pd
from pyecharts.charts import Line, Bar, Pie

from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.globals import CurrentConfig
from pyecharts.datasets import register_url

import styles

def draw_bar(data,title='两个省份其他字段分析', rotate=0):
    bar_chart = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK,
                                    width='1200px', height='800px'))
        .add_xaxis(data.index.tolist())
        .add_yaxis('湖北', [int(x) for x in data['湖北'].tolist()],
                bar_max_width='60%',
                category_gap=0,
                itemstyle_opts=styles.get_area_style_color())
        .add_yaxis('湖南', [int(x) for x in data['湖南'].tolist()],
                bar_max_width='60%',
                itemstyle_opts=styles.get_area_style_color()
                )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),
            legend_opts=opts.LegendOpts(
                is_show=True, textstyle_opts=opts.TextStyleOpts(color='auto')),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger='axis', axis_pointer_type='shadow'),
            xaxis_opts=opts.AxisOpts(
                splitline_opts={"show": False},
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='white')),
                axislabel_opts=opts.LabelOpts(color='white', font_weight='bold', rotate=rotate),
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts={"show": True},
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='white')),
                axislabel_opts=opts.LabelOpts(color='white', font_weight='bold'),
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True,
                font_weight='bold', position='top'
                                        ))
    )

    return bar_chart

def draw_pie(data, title):
    pie = (Pie()
        .add("湖北", data['湖北'].reset_index().values.tolist(),
            radius=["25%", "45%"], center=["25%", "50%"])
        .add("湖南", data['湖南'].reset_index().values.tolist(),
            radius=["25%", "45%"], center=["75%", "50%"])
        )
    return pie

if __name__ == '__main__':
