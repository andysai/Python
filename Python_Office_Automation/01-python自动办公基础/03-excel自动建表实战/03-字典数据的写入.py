# 导入模块
import xlrd
import xlwt

# 创建工作簿
workbook = xlwt.Workbook()
# 创建工作表
worksheet = workbook.add_sheet("零食售卖清单")


goods = {"商品id":["品名","数量","单位","单价","总价"],
          21323:["面包",5,"包",23],
          46456:["鸡蛋卷",4,"包",42],
          45645:["鸡翅",1,"千克",33],
          754557:["牛肉干",2,"千克",45],
          456456:["火腿肠",4,"箱",67],
          456546:["巧克力",2,"箱",49],
          73454:["山楂",4,"箱",44],
          234:["鸡肉",23,"千克",56]}
i = 0
for key,value in goods.items():
    # 将字典中的键放在第0列
    worksheet.write(i,0,key)
    # 写入i行，列表的下表+1列，写入的数据:列表下表对应的元素
    for j in range(len(value)):
        worksheet.write(i,j+1,value[j])
    i += 1


# 保存
workbook.save("../source_material/零食售卖清单.xls")