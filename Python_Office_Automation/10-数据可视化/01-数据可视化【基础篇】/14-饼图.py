from pyecharts.faker import Faker
from pyecharts.charts import Pie
import pyecharts.options as opts

pie = Pie()

#pie.add('饼图',[list(z) for z in zip(Faker.choose(),Faker.values())])
#pie.set_global_opts(title_opts=opts.TitleOpts(title='Pie-饼图'))
#pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))

pie.add(
    '饼图',
    [list(z) for z in zip(Faker.choose(),Faker.values())],
    # radius 表示内环和外环半径，列表类型
    radius=['40%', '75%'],
    # rosetype 设置玫瑰饼图模式, area所有扇区圆心角相同，仅通过半径展现数据大小
    rosetype='area'
)

pie.set_global_opts(title_opts=opts.TitleOpts(title='Pie-饼图'))
pie.set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))

pie.render('../source_material/01/14-玫瑰饼图.html')
print("生成成功")
