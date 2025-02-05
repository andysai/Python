import tkinter as tk
import random
import select_db


def update_label():
    label.config(text=random.choice(select_db.select_table()))
    root.after(1000, update_label)  # 每1000毫秒（1秒）更新一次标签内容

root = tk.Tk()
label = tk.Label(root, font=('宋体', 48))
label.pack()

button = tk.Button(root, text="开始", command=update_label)
button.pack()

# stop = tk.Button(root, text="暂停", command=stop_label)
# stop.pack()
# update_label()  # 开始更新标签内容
root.mainloop()
