import requests
import re
import tkinter as tk  # GUI界面
import webbrowser  # 打开网站

url = 'http://www.qmaile.com/'
respond = requests.get(url)
respond.encoding = 'utf-8'
reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg, respond.text)
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
six = res[5]

root = tk.Tk()  # 启动窗口 TK类
root.title('全网通用Vip视频播放             作者——Jery')
root.geometry('500x300+600+250')  # 左边距与上边距
l1 = tk.Label(root, text='请选择接口:', font=12)
l1.grid(row=0, column=0)  # 控件网格布局
var = tk.StringVar()  # 传参功能，value值传给variable
r1 = tk.Radiobutton(root, text='接口1', variable=var, value=one)
r1.grid(row=0, column=1)
r2 = tk.Radiobutton(root, text='接口2', variable=var, value=two)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='接口3', variable=var, value=three)
r3.grid(row=2, column=1)
r4 = tk.Radiobutton(root, text='接口4', variable=var, value=four)
r4.grid(row=3, column=1)
r5 = tk.Radiobutton(root, text='接口5', variable=var, value=five)
r5.grid(row=4, column=1)
r6 = tk.Radiobutton(root, text='接口6', variable=var, value=six)
r6.grid(row=5, column=1)

l2 = tk.Label(root, text='播放链接:', font=12)
l2.grid(row=6, column=0)

e1 = tk.Entry(root, text='', width=50)
e1.grid(row=6, column=1)


def play():
    webbrowser.open(var.get() + e1.get())  # 总链接


def clear():
    e1.delete(0, 'end')


b1 = tk.Button(root, text='播放', font=12, width=8, command=play)
b1.grid(row=7, column=1)
b2 = tk.Button(root, text='清除', font=12, width=8, command=clear)
b2.grid(row=8, column=1)
root.mainloop()  # 循环显示