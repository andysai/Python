# coding=utf-8

f_name = 'text.txt'
with open(f_name, 'r') as f:
    lines = f.readlines()
    print(lines)
    copy_f_name = 'copy_text.txt'
    with open(copy_f_name, 'w') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')
        