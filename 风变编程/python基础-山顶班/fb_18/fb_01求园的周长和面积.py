# 如流程图所示，求圆的面积和周长的代码
# 圆周率(pi)取3.14即可
r = float(input('请输入圆的半径:'))
pi = 3.14
S = pi * r * r
L = 2 * pi * r
print('圆的面积为{} \n周长为{}'.format(S,L))