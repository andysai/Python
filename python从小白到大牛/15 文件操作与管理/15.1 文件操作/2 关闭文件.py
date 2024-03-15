# coding=utf-8

# 使用finaly关闭文件
f_name = 'text.txt'
try:
    f = open(f_name)
except OSError as e:
    print('打开文件失败')
else:
    print('打开文件成功')
    try:
        content = f.read()
        print(content)
    except OSError as e:
        print('处理OSError异常')
    finally:
        f.close()

# 使用with as 自动资源管理
with open(f_name, 'r') as f:
    content = f.read()
    print(content)