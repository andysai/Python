# coding=utf-8

f_name = 'coco2dxcplus.jpg'

with open(f_name, 'rb') as f:
    b = f.read()
    copy_f_name = 'copy.jpg'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')