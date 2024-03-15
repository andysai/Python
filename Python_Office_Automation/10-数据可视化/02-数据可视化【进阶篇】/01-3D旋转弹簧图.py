import math
from pyecharts import options as opts
from pyecharts.charts import Line3D
from pyecharts.faker import Faker

data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t ) * math.cos(_t))
    y = (1 + 0.25 * math.cos(75 * _t ) * math.sin(_t))
    z = _t + 2.0 * math.sin(75 * _t)
    data.append([x, y, z])
c = (
    Line3D(init_opts=opts.InitOpts(width='1600px',height='620px'))
    .add(
        "",
        data,
        xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
        grid3d_opts=opts.Grid3DOpts(
            width=100, depth=100, rotate_speed=150, is_rotate=True
        ),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=30, min_=0, range_color=Faker.visual_color
        ),
        title_opts=opts.TitleOpts(title="Line3D-旋转的弹簧"),
    )
    .render("../source_material/02/01-line3d_旋转的弹簧.html")
)
print("=========================生成成功============================")