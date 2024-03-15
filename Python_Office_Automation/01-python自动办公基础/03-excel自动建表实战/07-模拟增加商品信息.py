# 导入模块
import xlrd
import xlwt
import random

# 创建工作簿
workbook = xlwt.Workbook()
# 创建工作表
worksheet = workbook.add_sheet("零食售卖清单")

# 设置样式0
def style0():
    # 初始化样式(创建样式对象)
    style = xlwt.XFStyle()
    # 创建字体属性对象
    font = xlwt.Font()
    font.name = "宋体"
    font.bold = False
    font.height = 20*14
    style.font = font

    # 创建边界属性对象
    borders = xlwt.Borders()
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    style.borders = borders

    # 创建对齐属性对象
    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    style.alignment = alignment

    # 创建模式属性对象
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 44
    style.pattern = pattern

    # 调用风格样式
    return style

# 设置样式1
def style1():
    # 初始化样式(创建样式对象)
    style = xlwt.XFStyle()
    # 创建字体属性对象
    font = xlwt.Font()
    font.name = "宋体"
    font.bold = False
    font.height = 20*14
    style.font = font

    # 创建边界属性对象
    borders = xlwt.Borders()
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    style.borders = borders

    # 创建对齐属性对象
    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    style.alignment = alignment

    # 创建模式属性对象
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 23
    style.pattern = pattern

    # 调用风格样式
    return style

# 设置样式2
def style2():
    # 初始化样式(创建样式对象)
    style = xlwt.XFStyle()
    # 创建字体属性对象
    font = xlwt.Font()
    font.name = "宋体"
    font.bold = False
    font.height = 20*14
    style.font = font

    # 创建边界属性对象
    borders = xlwt.Borders()
    borders.top = 1
    borders.bottom = 1
    borders.left = 1
    borders.right = 1
    style.borders = borders

    # 创建对齐属性对象
    alignment = xlwt.Alignment()
    alignment.vert = xlwt.Alignment.VERT_CENTER
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    style.alignment = alignment

    # 创建模式属性对象
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 1
    style.pattern = pattern

    # 调用风格样式
    return style

style0 = style0()
style1 = style1()
style2 = style2()

# 整理数据
# goods = {"商品id":["品名","数量","单位","单价","总价"],
#           21323:["面包",5,"包",23],
#           46456:["鸡蛋卷",4,"包",42],
#           45645:["鸡翅",1,"千克",33],
#           754557:["牛肉干",2,"千克",45],
#           456456:["火腿肠",4,"箱",67],
#           456546:["巧克力",2,"箱",49],
#           73454:["山楂",4,"箱",44],
#           234:["鸡肉",23,"千克",56]}
def get_goods():
    goods = {}
    goods["商品id"] = ["品名", "数量", "单位", "单价", "总价"]
    for i in range(250):
        pinming = random.choice(["鸡","鸭","鱼","螃蟹","虾"]) + "肉"
        shuliang = random.randint(1,5)
        danwei = random.choice(["包","千克","箱"])
        danjia = random.randint(10,100)
        lists = [pinming, shuliang, danwei,danjia]
        goods[random.randint(10000,99999)] = lists
    return goods
goods = get_goods()


# 写入数据
i = 0
for key,value in goods.items():
    # 设置列宽
    worksheet.col(i).width = 256 * 20

    if i == 0:
        # 将字典中的键放在第0列
        worksheet.write(i,0,key,style0)
    elif i > 0 and i%2 ==1:
        worksheet.write(i,0,key,style1)
    else:
        worksheet.write(i,0,key,style2)

    # 写入i行，列表的下表+1列，写入的数据:列表下表对应的元素
    for j in range(len(value)):
        if i == 0:
            worksheet.write(i,j+1,value[j],style0)
        elif i > 0 and i%2 == 1:
            worksheet.write(i, j + 1, value[j],style1)
        else:
            worksheet.write(i, j + 1, value[j],style2)
    i += 1

# 计算总价
m = 0
for key,value in goods.items():
    if m > 0:
        if m % 2 == 1:
            worksheet.write(m, len(value)+1, value[1] * value[3],style1)
        else:
            worksheet.write(m, len(value) + 1, value[1] * value[3],style2)
    m += 1

# 保存
workbook.save("../source_material/零食售卖清单(1).xls")