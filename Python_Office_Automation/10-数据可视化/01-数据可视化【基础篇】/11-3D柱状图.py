from pyecharts.charts import Bar3D
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType
import random
bar3d = Bar3D(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width='1200px',
    height='720px'))
data = [(i,j,random.randint(0,12)) for i in range(20) for j in range(6)]
bar3d.add(
    '3D柱形图',
    data,
    xaxis3d_opts=opts.Axis3DOpts(Faker.clock,type_='category'),
    yaxis3d_opts=opts.Axis3DOpts(Faker.week_en,type_='category'),
    zaxis3d_opts=opts.Axis3DOpts(type_='value')
)
bar3d.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(max_=20),
    title_opts=opts.TitleOpts(title='Bar3D-柱形图')
)
bar3d.render('../source_material/01/3D柱形图.html')
print('生成成功')
