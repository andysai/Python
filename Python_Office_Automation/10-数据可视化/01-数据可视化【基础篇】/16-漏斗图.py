from pyecharts.faker import Faker
from pyecharts.charts import Funnel
import pyecharts.options as opts
from pyecharts.globals import SymbolType

funnel = Funnel()
funnel.add(
    '用户转化率',
    [list(z) for z in zip(Faker.choose(), Faker.values())],
    label_opts=opts.LabelOpts(position='inside')
)
funnel.set_global_opts(title_opts=opts.TitleOpts(title="Funnel-漏斗图"))
funnel.render('../source_material/01/16-漏斗图.html')
print('生成成功')
