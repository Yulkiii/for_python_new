import tkinter as tk
import tkinter.messagebox
import yagmail
import random
import time
import hashlib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
import xlwt

root = tk.Tk()  # 创建应用程序窗口
root.title("POP_FLY")
root.geometry("250x180")
send_requestw = tk.Tk()
w, h = send_requestw.maxsize()
send_requestw.geometry("{}x{}".format(w, h))
send_requestw.title("POP_FLY")
send_requestw.withdraw()
# --------功能块代码开始-------

# 功能函数设计
varName = tk.StringVar()
varName.set('')
varPwd = tk.StringVar()
varPwd.set('')


#############################################################################
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    # value = u'%s <%s>'name, addr)
            print("%s", value)


def get_mail_name(msg):
    for header in ['Subject']:
        value = msg.get(header, '')
        return value


def get_att(msg, path="return_d\\"):
    attachment_files = []
    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        contType = part.get_content_type()
        if file_name:
            print(file_name)
            filename = file_name
            data = part.get_payload(decode=True)  # 下载附件
            att_file = open(path + filename, 'wb')  # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    return attachment_files[0]


def check_mail_name(name_split):
    f = open("time.txt", "r", encoding="utf-8")
    time = f.read()
    time = time.split("\n")
    f.close
    try:
        if int(name_split[1]) > int(time[0]):
            new_time = name_split[1] + "\n" + name_split[2] + "\n" + name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        if int(name_split[2]) > int(time[1]):
            new_time = name_split[1] + "\n" + name_split[2] + "\n" + name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        if int(name_split[3]) > int(time[2]) + 1:
            new_time = name_split[1] + "\n" + name_split[2] + "\n" + name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        return 0
    except BaseException:
        print("none")
        return 0


def send_mail(type_of, attachment):
    time1 = time.strftime('%Y/%m%d/%H%M%S', time.localtime(time.time()))
    username = '2268670833@qq.com'  # 邮箱账号
    passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
    mail = yagmail.SMTP(user=username,
                        password=passwd,
                        host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                        smtp_ssl=True
                        )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
    mail.send(
        to=['3067842904@qq.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
        # cc='735557314@qq.com',  # 抄送
        subject=type_of + '/' + str(time1),  # 邮件标题
        contents='',
        attachments=attachment)


def send_mail2(mail_account, attachment='', subject1='', content=''):
    time1 = time.strftime('%Y/%m%d/%H%M%S', time.localtime(time.time()))
    username = '2268670833@qq.com'  # 邮箱账号
    passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
    mail = yagmail.SMTP(user=username,
                        password=passwd,
                        host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                        smtp_ssl=True
                        )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
    mail.send(
        to=[mail_account],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
        # cc='735557314@qq.com',  # 抄送
        subject=subject1,  # 邮件标题
        contents=content,
        attachments=attachment)


def log_in_mail():
    email = '2268670833@qq.com'
    password = 'gvdcodoqyfdudhgd'
    pop3_server = 'pop.qq.com'
    server = poplib.POP3(pop3_server)
    server.set_debuglevel(1)
    server.user(email)
    server.pass_(password)
    resp, mails, octets = server.list()
    index = len(mails)
    resp, lines, octets = server.retr(index)
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    mail_name = get_mail_name(msg)
    mail_name_split = mail_name.split('/')
    return mail_name_split, msg


#########################################################################
def login():
    # 获取用户名和密码11250906
    name = entryName.get()
    send_request(name)
    if len(name)!=8:
    	tkinter.messagebox.askyesno('noting:', 'Task number should be 8 bits!')
    	return
    for i in range(len(name)):
    	if name[i]<"0" or name[i]>"9":
    		tkinter.messagebox.askyesno('noting:', 'Task number input error!')
    		return
    filename="task\\"+name+".txt"
    f = open(filename, "w", encoding="utf-8")
    f.close()
    f = open("time.txt", "w", encoding="utf-8")
    time1 = time.strftime('%Y\n%m%d\n%H%M%S', time.localtime(time.time()))
    f.write(time1)
    f.close()
    send_mail("t",filename)
    tkinter.messagebox.askyesno('noting:', 'please wait, at most 10 seconds,and please press ok')
    while True:
        mail_name_split, msg = log_in_mail()
        print(mail_name_split)
        if check_mail_name(mail_name_split):
            if mail_name_split[0] == "d":
                file_name = get_att(msg)
                if(file_name=="0.txt"):
                	tkinter.messagebox.askyesno('noting:', 'no such Task number !')
                	return
                else:
                	send_request(name)

def cancel():
    # 清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')
def _quit():
    root.quit()
    root.destroy()
#################################################################################################################################
labelnone = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1, height=2).grid(column=0, row=1)
labelnone2 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=2)
labelnone3 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=3)
labelnone4 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=4)
labelcata = tk.Label(send_requestw, text='                       Catalogue', justify=tk.LEFT, width=180)
labelamm = tk.Label(send_requestw, text='ammount', justify=tk.RIGHT, width=200)
labelshop = tk.Label(send_requestw, text='shopping address', justify=tk.RIGHT, width=200)
labelcost = tk.Label(send_requestw, text='cost in total', justify=tk.RIGHT, width=80)
labelothers = tk.Label(send_requestw, text='others', justify=tk.RIGHT, width=120)
labelcheck = tk.Label(send_requestw, text='check', justify=tk.RIGHT, width=120)
labelcata.place(x=0, y=10, width=160, height=20)
labelamm.place(x=10 + 300, y=10, width=180, height=20)
labelshop.place(x=10 + 300 * 2, y=10, width=180, height=20)
labelcost.place(x=10 + 300 * 3, y=10, width=60, height=20)
labelothers.place(x=10 + 300 * 3+120, y=10, width=120, height=20)
labelcheck.place(x=10 + 300 * 3+120+250, y=10, width=60, height=20)

def send_request(account):
    name="return_d//"+"11251014"+".txt"
    file=open(name,"r",encoding="utf-8")
    f=file.read()
    f=f.split("\n")
    for i in range(len(f)-1):
        f2=f[i+1]
        f2=f2.split("/")
        name1 = 'entrycata' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80)
        globals()[name1].insert(0, f2[0])
        globals()[name1].place(x=40, y=34 + 25 * int(i), width=300, height=20)
        name1 = 'entryamm' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80)
        globals()[name1].insert(0, f2[1])
        globals()[name1].place(x=40 + 300, y=34 + 25 * int(i), width=300, height=20)
        name1 = 'entryshop' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80)
        globals()[name1].insert(0, f2[2])
        globals()[name1].place(x=40 + 2 * 300, y=34 + 25 * int(i), width=240, height=20)
        name1 = 'entrycost' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80)
        globals()[name1].insert(0, f2[3])
        globals()[name1].place(x=40 + 3 * 300-60, y=34 + 25 * int(i), width=120, height=20)
        name1 = 'entryothers'+ str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80)
        if(f2[4]=="*"):
            f2[4]=""
        globals()[name1].insert(0, f2[4])
        globals()[name1].place(x=40 + 3 * 300+60, y=34 + 25 * int(i), width=250, height=20)
        name = 'check' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entrycheck' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 3 * 300+60+250, y=34 + 25 * int(i), width=100, height=20)
     

    def exit():
        if (tkinter.messagebox.askyesno(title='POP_FLY', message='ensure quit')) == False:
            return
        send_requestw.quit()
        send_requestw.destroy()
        root.quit()
        root.destroy()
        register_win.quit()
        register_win.destroy()
    def send_to_host():
        f = open("send\\" + name + ".txt", "w", encoding="utf-8")
        str1=''
        for i in range(len(f)-1):
            name = "entrycata" + str(i)
            
        f.write(str1)
        f.close()
        send_mail2('3067842904@qq.com', "send\\" + account + ".xls", subject1='',
                   content='Hellow ,Welcome to use POPFLY')
        send_mail("c", "send\\" + account + ".txt")

    def back():
        send_requestw.quit()
        send_requestw.withdraw()
        root.deiconify()

    def empty():
        name="return_d//"+"11251014"+".txt"
        file=open(name,"r",encoding="utf-8")
        f=file.read()
        f=f.split("\n")
        for i in range(len(f)-1):
            f2=f[i+1]
            f2=f2.split("/")
            name1 = 'entrycata' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80)
            globals()[name1].insert(0, f2[0])
            globals()[name1].place(x=40, y=34 + 25 * int(i), width=300, height=20)
            name1 = 'entryamm' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80)
            globals()[name1].insert(0, f2[1])
            globals()[name1].place(x=40 + 300, y=34 + 25 * int(i), width=300, height=20)
            name1 = 'entryshop' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80)
            globals()[name1].insert(0, f2[2])
            globals()[name1].place(x=40 + 2 * 300, y=34 + 25 * int(i), width=240, height=20)
            name1 = 'entrycost' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80)
            globals()[name1].insert(0, f2[3])
            globals()[name1].place(x=40 + 3 * 300-60, y=34 + 25 * int(i), width=120, height=20)
            name1 = 'entryothers'+ str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80)
            if(f2[4]=="*"):
                f2[4]=""
            globals()[name1].insert(0, f2[4])
            globals()[name1].place(x=40 + 3 * 300+60, y=34 + 25 * int(i), width=250, height=20)
            name = 'check' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entrycheck' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 3 * 300+60+250, y=34 + 25 * int(i), width=100, height=20)
     
    root.quit()
    send_requestw.deiconify()
    menubar = tk.Menu(send_requestw)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemen1 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Command', menu=filemenu)
    filemenu.add_command(label="back", command=back)
    filemenu.add_command(label='send to host', command=send_to_host)
    filemenu.add_command(label='exit', command=exit)
    filemenu.add_command(label='renew all', command=empty)
    send_requestw.config(menu=menubar)
    send_requestw.mainloop()


#################################################################################################################################
# 主窗口中的各个组件设计
labelName = tk.Label(root, text='task number：', justify=tk.RIGHT, width=100)
entryName = tk.Entry(root, width=80, textvariable=varName)
buttonOk = tk.Button(root, text='ensure            ', relief=tk.RAISED, command=login)
buttonCancel = tk.Button(root, text='delete all', relief=tk.RAISED, command=cancel)
buttonquit = tk.Button(root, text='quit', relief=tk.RAISED, command=_quit)
# 主窗口中各个组件的排放位置 = 排兵布阵
labelName.place(x=10, y=5, width=80, height=20)
entryName.place(x=100, y=5, width=80, height=20)
buttonOk.place(x=30, y=70, width=50, height=20)
buttonCancel.place(x=90, y=70, width=50, height=20)
buttonquit.place(x=150, y=70, width=50, height=20)
# --------功能块代码结束------
root.mainloop()  # 窗口运行循环
