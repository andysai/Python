# 导入库
from pyecharts.charts import Bar

# 实例化对象，初始化柱形图
bar = Bar()

# x轴显示的数据
x = ["葡萄", "橘子", "香蕉", "榴莲", "苹果", "梨"]

# y轴显示的数据
y = [123, 32, 56, 99, 210, 100]

# 在x、y轴上添加数据
bar.add_xaxis(x)
bar.add_yaxis("水果", y)

# 生成数据图表并为图表命名
bar.render("../source_material/01/02-柱状图.html")
print("执行成功")
