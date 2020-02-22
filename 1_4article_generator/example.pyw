from bullshit import generator
import tkinter as tk
import tkinter.messagebox
import time
root = tk.Tk()  # 启动窗口 TK类
root.title('AG-author:BIZHI')
root.geometry('300x200+600+250')  # 左边距与上边距

l2 = tk.Label(root, text='TITLE OF ARTICLE', font=16)
l2.grid(row=0, column=0)

e1 = tk.Entry(root, text='', width=50)
e1.grid(row=1, column=0)

l3 = tk.Label(root, text='LENGTH OF ARTICLE', font=16)
l3.grid(row=2, column=0)

e2 = tk.Entry(root, text='1000', width=50)
e2.grid(row=3, column=0)

def play():
    try:
        if e1.get()=='' or e2.get()=='':
            tkinter.messagebox.showinfo('NOTING','Input cannot be empty')
        else:
            content=e1.get()+'\n'
            content+= generator(e1.get(), length=int(e2.get()))+'\n'
            content+="综上，对于这个人类不得不深思。"
            time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            path=str(time1)+'.txt'
            f=open(path,'w')
            f.write(content)
            f.close()
            tkinter.messagebox.showinfo('NOTING','File saved at the same folder, name:'+str(path))
    except BaseException:
        tkinter.messagebox.showinfo('NOTING','Input length should be integer')
        pass
        

def clear():
    e1.delete(0, 'end')
    e2.delete(0, 'end')

b1 = tk.Button(root, text='START GENERATE ARTICLE', font=16, width=25, command=play)
b1.grid(row=4, column=0)
b2 = tk.Button(root, text='DELETE ALL', font=16, width=25, command=clear)
b2.grid(row=5, column=0)
root.mainloop() 

