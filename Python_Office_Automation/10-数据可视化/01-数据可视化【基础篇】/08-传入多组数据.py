from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 设置图表大小
bar = Bar(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width='1000px',
    height='720px'))
x = ['葡萄', '橘子', '香蕉', '榴莲', '苹果', '梨']
y1 = [123, 32, 56, 99, 210, 100]
y2 = [100, 132, 46, 69, 90, 120]
bar.add_xaxis(x)
bar.add_yaxis('水果1', y1)
bar.add_yaxis('水果2', y2)
# 将数据堆叠在一起，可以将两两数据进行堆叠,用stack方法
#bar.add_yaxis('水果1',y1,stack='stack1')
#bar.add_yaxis('水果2',y2,stack='stack1')

bar.set_global_opts(title_opts=opts.TitleOpts(
    title='水果数量',
    subtitle='副标题'))

bar.render('../source_material/01/08-两组数据.html')
print("执行成功")
