from pyecharts.faker import Faker
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
line.add_xaxis(Faker.choose())
# is_smooth 是否让折线变平滑
line.add_yaxis('商家A',
               Faker.values(),
               is_smooth=True,
               areastyle_opts=opts.AreaStyleOpts(
                   opacity=0.2,
                   color={'type': 'linear', 'x': 0, 'y': 0, 'x2': 0, 'y2': 1, 'colorStops': [{'offset': 0, 'color': 'red'}, {'offset': 1, 'color': 'blue'}]}))
line.add_yaxis('商家B', Faker.values())
line.set_global_opts(title_opts=opts.TitleOpts(title='折线图'))
line.render('../source_material/01/13-渐变折线图.html')
print('生成成功')

