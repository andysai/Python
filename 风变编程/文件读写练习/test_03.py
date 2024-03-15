# 假设感觉有困难，可查看步骤中的提示（鼠标移到步骤小标题上点击出现的问号）。
#请你通过文件读写命令，读取 photo1 里的数据（提示见代码区开头）。
#然后，新建名为“photo2”的图片（在同一个文件夹），写入读到的数据。
#这样，我们就通过文件读写的代码，完成了图片的复制（而非鼠标右键）。
with open('photo1.png','rb') as file:
    pf = file.read()
    with open('photo2.png','wb') as new_file:
        new_file.write(pf)