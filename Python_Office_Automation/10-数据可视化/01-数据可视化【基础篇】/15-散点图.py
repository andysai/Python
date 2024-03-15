from pyecharts.faker import Faker
from pyecharts.charts import EffectScatter
import pyecharts.options as opts
from pyecharts.globals import SymbolType

effect_scatter = EffectScatter()
effect_scatter.add_xaxis(Faker.choose())
effect_scatter.add_yaxis(
    '散点图',
    Faker.values(),
    symbol=SymbolType.DIAMOND
)
effect_scatter.set_global_opts(title_opts=opts.TitleOpts(title='EffectScatter-散点图'))
effect_scatter.render('../source_material/01/15-动态散点图.html')
print('生成成功')
