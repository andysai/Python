from pyecharts.faker import Faker
from pyecharts.charts import Geo
import pyecharts.options as opts
from pyecharts.globals import ThemeType

geo = Geo(init_opts=opts.InitOpts(
    theme=ThemeType.PURPLE_PASSION,
    width='1600px',
    height='800px'))
geo.add_schema(maptype='china')
geo.add('geo',
        [list(z) for z in zip(Faker.provinces,Faker.values())],
        type_='heatmap'
        )
geo.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(),
    title_opts=opts.TitleOpts(title='Geo-地图')
)
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.render('../source_material/01/17-地图.html')
print("生成成功")
