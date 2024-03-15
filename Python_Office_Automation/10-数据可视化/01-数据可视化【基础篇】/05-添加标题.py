from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
x = ['葡萄', '橘子', '香蕉', '榴莲', '苹果', '梨']
y = [123, 32, 56, 99, 210, 100]
bar.add_xaxis(x)
bar.add_yaxis('水果', y)
bar.set_global_opts(title_opts=opts.TitleOpts(title='水果数量', subtitle='副标题'))
bar.render('../source_material/01/05-添加标题.html')
print("执行成功")
