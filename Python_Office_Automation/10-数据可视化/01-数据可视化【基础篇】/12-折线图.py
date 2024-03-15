from pyecharts.faker import Faker
from pyecharts.charts import Line
import pyecharts.options as opts

line = Line()
line.add_xaxis(Faker.choose())
# is_smooth 是否让折线变平滑
line.add_yaxis('商家A', Faker.values(), is_smooth=True)
line.add_yaxis('商家B', Faker.values())
line.set_global_opts(title_opts=opts.TitleOpts(title='折线图'))
line.render('../source_material/01/12-折线图.html')
print('生成成功')
