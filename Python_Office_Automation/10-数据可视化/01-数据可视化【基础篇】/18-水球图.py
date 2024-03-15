from pyecharts.charts import Liquid
import pyecharts.options as opts

liquid = Liquid()
# is_outline_show 是否显示外边框
# is_animation 是否显示动画效果
# shape 边框形状，和symbol可用的形状类似，还可以自定义
liquid.add('水球图', [0.7, 0.6, 0.5])
liquid.set_global_opts(title_opts=opts.TitleOpts(title='Liquid-水球图'))
liquid.render('../source_material/01/18-水球图.html')
print('成功创建')
