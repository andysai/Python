from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
bar = Bar(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width='480px',
    height='320px'))
x = ['葡萄', '橘子', '香蕉', '榴莲', '苹果', '梨']
y = [123, 32, 56, 99, 210, 100]
bar.add_xaxis(x)
bar.add_yaxis('水果', y)
bar.set_global_opts(title_opts=opts.TitleOpts(
    title='水果数量',
    subtitle='副标题'),
    # -90°到90°
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)))
bar.render('../source_material/01/07-旋转x轴.html')
print("执行成功")
