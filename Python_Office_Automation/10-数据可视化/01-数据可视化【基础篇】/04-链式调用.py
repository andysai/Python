from pyecharts.charts import Bar

x = ['葡萄', '橘子', '香蕉', '榴莲', '苹果', '梨']
y = [123, 32, 56, 99, 210, 100]

Bar().add_xaxis(x).add_yaxis('水果', y).render('../source_material/01/04-链式调用.html')
print("执行成功")
