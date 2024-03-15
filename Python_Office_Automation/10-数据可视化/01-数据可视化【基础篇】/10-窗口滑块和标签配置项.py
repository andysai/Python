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
# 设置标题
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title='水果数量',
        subtitle='副标题'),
    # 设置窗口滑块
    datazoom_opts=[opts.DataZoomOpts()]
    )
# 设置标记点和标记线
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=False),
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_='max', name='最大值'),
            opts.MarkPointItem(type_='min', name='最小值')
            ]
        ),
    markline_opts=opts.MarkLineOpts(
        data=[opts.MarkPointItem(type_='average',name='平均值')]
        )
    )
bar.render('../source_material/01/10-窗口滑块.html')
print("执行成功")
