

from pyecharts.charts import Bar
from pyecharts.options import LabelOpts

bar = Bar()

bar.add_xaxis(["周一","周二","周三"])
bar.add_yaxis("每天的工作量",[10,20,30],
              label_opts = LabelOpts(position = "right"))

#x,y轴的反转
bar.reversal_axis()
#生成图表
bar.render()
