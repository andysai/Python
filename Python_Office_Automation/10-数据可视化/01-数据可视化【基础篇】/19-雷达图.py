from pyecharts.charts import Radar
import pyecharts.options as opts
from pyecharts.globals import ThemeType
radar = Radar(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width='1000px',
    height='700px'))
v1 = [
    [4300, 31560, 28000, 25626, 19000, 15000],
    [3300, 30000, 26000, 25000, 17000, 16000]
]
v2 = [[5000, 14000, 25000, 19000, 35000, 18000]]
radar.add_schema(
    schema=[
        opts.RadarIndicatorItem(name='销售', max_=6500),
        opts.RadarIndicatorItem(name='管理', max_=16000),
        opts.RadarIndicatorItem(name='信息技术', max_=9900),
        opts.RadarIndicatorItem(name='客服', max_=6900),
        opts.RadarIndicatorItem(name='研发', max_=18000),
        opts.RadarIndicatorItem(name='市场', max_=12600)
    ]
)
radar.add('预算分配', v1)
radar.add('实际开销', v2)
radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
radar.set_global_opts(title_opts=opts.TitleOpts(title='Radar-雷达图'))
radar.render('../source_material/01/19-雷达图.html')
print('生成成功')
