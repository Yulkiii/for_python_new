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
register_win = tk.Tk()
register_win.title("register")
register_win.geometry("300x300")
register_win.withdraw()
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


def get_att(msg, path="return_C\\"):
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
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    #########################
    root.quit()
    root.withdraw()
    send_request(name)
    ####################
    if len(name) > 9 or len(name) < 8:
        tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
        return
    elif len(pwd) < 6:
        tkinter.messagebox.askyesno('noting:', 'passward at least 6 numbers or characters')
        return
    solution = "log_in\\" + name + ".txt"
    m = hashlib.sha1()
    byte = '1'.join(format(ord(x), 'b') for x in pwd)
    m.update(byte.encode())
    f = open(solution, "w", encoding="utf-8")
    f = open(solution, "a", encoding="utf-8")
    f.write(name + "\n" + m.hexdigest())
    f.close()
    tkinter.messagebox.askyesno('noting:', 'please wait, at most 10 seconds,and please press ok')
    send_mail("b", solution)
    while True:
        mail_name_split, msg = log_in_mail()
        print(mail_name_split)
        if check_mail_name(mail_name_split):
            if mail_name_split[0] == "c":
                file_name = get_att(msg)
                print(file_name)
                f = open("return_c\\" + file_name, "r", encoding="utf-8")
                read = f.read()
                print(read)
                if read == '0':
                    tkinter.messagebox.askyesno('noting:', 'passward error')
                    return
                elif read == '1':
                    tk.messagebox.showinfo(title='noting', message='loged in')
                    send_request(name)
                elif read == '-1':
                    tkinter.messagebox.askyesno('noting:', 'account error')
                    return


def cancel():
    # 清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')


def _quit():
    root.quit()
    root.destroy()


def register():
    register_win.deiconify()
    global code
    global solution

    def ensure():
        global code
        ensurecode = entryverify.get()
        ensurepass1 = entryPwdreg.get()
        ensurepass2 = entryPwdrereg.get()
        ensureaccount = entryNamereg.get()
        ensuremail = entryemail.get()
        for x in ensureaccount:
            if x < '0' or x > '9':
                tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
                return
        if ensurepass1 != ensurepass2:
            tkinter.messagebox.askyesno('noting:', 'passward is not the same')
            return
        elif len(ensureaccount) > 9 or len(ensureaccount) < 8:
            tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
            return
        elif len(ensurepass1) < 6:
            tkinter.messagebox.askyesno('noting:', 'passward too short, at least 6 numbers or characters')
            return
        else:
            if ensurecode == str(code):
                solution = "log\\" + ensureaccount + ".txt"
                m = hashlib.sha1()
                byte = '1'.join(format(ord(x), 'b') for x in ensurepass1)
                m.update(byte.encode())
                f = open(solution, "w", encoding="utf-8")
                f = open(solution, "a", encoding="utf-8")
                f.write(ensureaccount + "\n" + m.hexdigest() + "\n" + ensuremail + '\n0')
                f.close()
                time1 = time.strftime('%Y/%m%d/%H%M%S', time.localtime(time.time()))
                username = '2268670833@qq.com'  # 邮箱账号
                passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
                account = entryemail.get()
                mail = yagmail.SMTP(user=username,
                                    password=passwd,
                                    host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                                    smtp_ssl=True
                                    )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
                mail.send(
                    to=['3067842904@qq.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
                    # cc='735557314@qq.com',  # 抄送
                    subject='a/' + str(time1),  # 邮件标题
                    contents='',
                    attachments=solution)
                tkinter.messagebox.askyesno('noting:', 'register successfully')
                register_win.quit()
                register_win.destroy()
                root.destroy()
            else:
                tkinter.messagebox.askyesno('noting:', 'incorrect code')

    def send_code():
        try:
            ensuremail = entryemail.get()
            global code
            global solution
            code = random.randint(1000, 9999)
            username = '2268670833@qq.com'  # 邮箱账号
            passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
            account = entryemail.get()
            mail = yagmail.SMTP(user=username,
                                password=passwd,
                                host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                                smtp_ssl=True
                                )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
            mail.send(
                to=[account],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
                # cc='735557314@qq.com',  # 抄送
                subject="Hello",  # 邮件标题
                contents='your verification code is ' + str(code) + "\n thanks for using MailFly "
                # attachments=solution)
            )
            # 邮件正文
        except BaseException:
            tkinter.messagebox.askyesno('noting:', 'invavid mail account')
            return

    def back():
        register_win.quit()
        register_win.withdraw()
        root.update()
        root.deiconify()

    # root.quit()
    root.withdraw()
    regName = tk.StringVar()
    regName.set('')
    regPwd = tk.StringVar()
    regPwd.set('')
    regPwdre = tk.StringVar()
    regPwdre.set('')
    regmail = tk.StringVar()
    regmail.set('')
    regverify = tk.StringVar()
    regverify.set('')
    labelNamereg = tk.Label(register_win, text='Account：', justify=tk.RIGHT, width=80)
    labelPwdreg = tk.Label(register_win, text='Passward：', justify=tk.RIGHT, width=80)
    labelPwdrereg = tk.Label(register_win, text='rePassward：', justify=tk.RIGHT, width=80)
    labelemail = tk.Label(register_win, text='Email：', justify=tk.RIGHT, width=80)
    labelverify = tk.Label(register_win, text='Verify_code：', justify=tk.RIGHT, width=80)
    entryNamereg = tk.Entry(register_win, width=80, textvariable=regName)
    entryPwdreg = tk.Entry(register_win, show='*', width=80, textvariable=regPwd)
    entryPwdrereg = tk.Entry(register_win, show='*', width=80, textvariable=regPwdre)
    entryemail = tk.Entry(register_win, width=80, textvariable=regmail)
    entryverify = tk.Entry(register_win, width=80, textvariable=regverify)
    buttonget = tk.Button(register_win, text='Get_verify_code', relief=tk.RAISED, command=send_code)
    buttonback = tk.Button(register_win, text='Back', relief=tk.RAISED, command=back)
    buttonyes = tk.Button(register_win, text='Ensure', relief=tk.RAISED, command=ensure)
    labelNamereg.place(x=10, y=5, width=80, height=20)
    labelPwdreg.place(x=10, y=30, width=80, height=20)
    labelPwdrereg.place(x=10, y=60, width=80, height=20)
    labelemail.place(x=10, y=60 + 30, width=80, height=20)
    labelverify.place(x=10, y=120 + 30, width=80, height=20)
    entryNamereg.place(x=100, y=5, width=150, height=20)
    entryPwdreg.place(x=100, y=30, width=150, height=20)
    entryPwdrereg.place(x=100, y=60, width=150, height=20)
    entryemail.place(x=100, y=60 + 30, width=150, height=20)
    entryverify.place(x=100, y=120 + 30, width=50, height=20)
    buttonget.place(x=10, y=90 + 30, width=100, height=20)
    buttonback.place(x=10, y=150 + 30, width=50, height=20)
    buttonyes.place(x=10, y=180 + 30, width=50, height=20)
    register_win.mainloop()


#################################################################################################################################
labelnone = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1, height=2).grid(column=0, row=1)
labelnone2 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=2)
labelnone3 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=3)
labelnone4 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=4)
labelcata = tk.Label(send_requestw, text='                       Catalogue', justify=tk.LEFT, width=180)
labelamm = tk.Label(send_requestw, text='ammount', justify=tk.RIGHT, width=200)
labelshop = tk.Label(send_requestw, text='shopping address', justify=tk.RIGHT, width=200)
labelcost = tk.Label(send_requestw, text='cost in total', justify=tk.RIGHT, width=200)
labelothers = tk.Label(send_requestw, text='others', justify=tk.RIGHT, width=200)
labelcata.place(x=0, y=10, width=160, height=20)
labelamm.place(x=10 + 300, y=10, width=180, height=20)
labelshop.place(x=10 + 300 * 2, y=10, width=180, height=20)
labelcost.place(x=10 + 300 * 3, y=10, width=180, height=20)
labelothers.place(x=10 + 300 * 4, y=10, width=180, height=20)


def send_request(account):
    for i in range(32):
        # name="select"+str(i)
        # globals()[name]= tk.IntVar()
        # name1 = 'entryselect' + str(i)
        # globals()[name1]=tk.Checkbutton(send_requestw, text='',onvalue = 1, offvalue = 0,variable=globals()[name])
        # globals()[name1].deselect()
        # globals()[name1].grid(column=0, row=i+2)

        name = 'cata' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entrycata' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40, y=34 + 25 * int(i), width=300, height=20)
        name = 'amm' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryamm' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'shop' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryshop' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 2 * 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'cost' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entrycost' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 3 * 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'others' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryothers' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 4 * 300, y=34 + 25 * int(i), width=150, height=20)

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
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('sheet1')
        ws.write(0, 0, label='catalague')
        ws.write(0, 1, label='ammount')
        ws.write(0, 2, label='shopping address')
        ws.write(0, 3, label='cost')
        ws.write(0, 4, label='others')
        f = open("send\\" + account + ".txt", "w", encoding="utf-8")
        str1 = "catalogue/ammount/shopping address/cost/others\n"
        for i in range(32):
            name = "entrycata" + str(i)
            print(globals()[name].get())
            if (globals()[name].get() != ""):
                name = "entrycata" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'catalogue' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 0, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryamm" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'ammount' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 1, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryshop" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'shopping address' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 2, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entrycost" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'cost' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 3, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryothers" + str(i)
                if (globals()[name].get() == ""):
                    str1 += "*" + "\n"
                    ws.write(1 + i, 4, label="None")
                else:
                    str1 += globals()[name].get() + "\n"
                    ws.write(1 + i, 4, label=globals()[name].get())
        wb.save("send\\" + account + ".xls")
        f.write(str1)
        send_mail2('3067842904@qq.com', "send\\" + account + ".xls", subject1='',
                   content='Hellow ,Welcome to use POPFLY')

    def back():
        send_requestw.quit()
        send_requestw.withdraw()
        root.deiconify()

    def empty():
        for i in range(40):
            name = 'cata' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entrycata' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40, y=30 + 20 * int(i), width=300, height=20)
            name = 'amm' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryamm' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'shop' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryshop' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 2 * 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'cost' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entrycost' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 3 * 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'others' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryothers' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 4 * 300, y=30 + 20 * int(i), width=150, height=20)

    root.quit()
    send_requestw.deiconify()
    menubar = tk.Menu(send_requestw)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemen1 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Command', menu=filemenu)
    filemenu.add_command(label="back", command=back)
    filemenu.add_command(label='send to host', command=send_to_host)
    filemenu.add_command(label='exit', command=exit)
    filemenu.add_command(label='empty all', command=empty)
    send_requestw.config(menu=menubar)
    send_requestw.mainloop()


#################################################################################################################################
# 主窗口中的各个组件设计
labelName = tk.Label(root, text='account：', justify=tk.RIGHT, width=100)
labelPwd = tk.Label(root, text='passward：', justify=tk.RIGHT, width=100)
entryName = tk.Entry(root, width=80, textvariable=varName)
entryPwd = tk.Entry(root, show='*', width=80, textvariable=varPwd)
buttonOk = tk.Button(root, text='log in', relief=tk.RAISED, command=login)
buttonCancel = tk.Button(root, text='delete all', relief=tk.RAISED, command=cancel)
buttonquit = tk.Button(root, text='quit', relief=tk.RAISED, command=_quit)
button_register = tk.Button(root, text='register', relief=tk.RAISED, command=register)
# 主窗口中各个组件的排放位置 = 排兵布阵
labelName.place(x=10, y=5, width=80, height=20)
labelPwd.place(x=10, y=30, width=80, height=20)
entryName.place(x=100, y=5, width=80, height=20)
entryPwd.place(x=100, y=30, width=80, height=20)
buttonOk.place(x=30, y=70, width=50, height=20)
buttonCancel.place(x=90, y=70, width=50, height=20)
buttonquit.place(x=150, y=70, width=50, height=20)
button_register.place(x=30, y=110, width=50, height=20)
# --------功能块代码结束------
root.mainloop()  # 窗口运行循环
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
register_win = tk.Tk()
register_win.title("register")
register_win.geometry("300x300")
register_win.withdraw()
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


def get_att(msg, path="return_C\\"):
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
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    #########################
    root.quit()
    root.withdraw()
    send_request(name)
    ####################
    if len(name) > 9 or len(name) < 8:
        tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
        return
    elif len(pwd) < 6:
        tkinter.messagebox.askyesno('noting:', 'passward at least 6 numbers or characters')
        return
    solution = "log_in\\" + name + ".txt"
    m = hashlib.sha1()
    byte = '1'.join(format(ord(x), 'b') for x in pwd)
    m.update(byte.encode())
    f = open(solution, "w", encoding="utf-8")
    f = open(solution, "a", encoding="utf-8")
    f.write(name + "\n" + m.hexdigest())
    f.close()
    tkinter.messagebox.askyesno('noting:', 'please wait, at most 10 seconds,and please press ok')
    send_mail("b", solution)
    while True:
        mail_name_split, msg = log_in_mail()
        print(mail_name_split)
        if check_mail_name(mail_name_split):
            if mail_name_split[0] == "c":
                file_name = get_att(msg)
                print(file_name)
                f = open("return_c\\" + file_name, "r", encoding="utf-8")
                read = f.read()
                print(read)
                if read == '0':
                    tkinter.messagebox.askyesno('noting:', 'passward error')
                    return
                elif read == '1':
                    tk.messagebox.showinfo(title='noting', message='loged in')
                    send_request(name)
                elif read == '-1':
                    tkinter.messagebox.askyesno('noting:', 'account error')
                    return


def cancel():
    # 清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')


def _quit():
    root.quit()
    root.destroy()


def register():
    register_win.deiconify()
    global code
    global solution

    def ensure():
        global code
        ensurecode = entryverify.get()
        ensurepass1 = entryPwdreg.get()
        ensurepass2 = entryPwdrereg.get()
        ensureaccount = entryNamereg.get()
        ensuremail = entryemail.get()
        for x in ensureaccount:
            if x < '0' or x > '9':
                tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
                return
        if ensurepass1 != ensurepass2:
            tkinter.messagebox.askyesno('noting:', 'passward is not the same')
            return
        elif len(ensureaccount) > 9 or len(ensureaccount) < 8:
            tkinter.messagebox.askyesno('noting:', 'account should be your student ID')
            return
        elif len(ensurepass1) < 6:
            tkinter.messagebox.askyesno('noting:', 'passward too short, at least 6 numbers or characters')
            return
        else:
            if ensurecode == str(code):
                solution = "log\\" + ensureaccount + ".txt"
                m = hashlib.sha1()
                byte = '1'.join(format(ord(x), 'b') for x in ensurepass1)
                m.update(byte.encode())
                f = open(solution, "w", encoding="utf-8")
                f = open(solution, "a", encoding="utf-8")
                f.write(ensureaccount + "\n" + m.hexdigest() + "\n" + ensuremail + '\n0')
                f.close()
                time1 = time.strftime('%Y/%m%d/%H%M%S', time.localtime(time.time()))
                username = '2268670833@qq.com'  # 邮箱账号
                passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
                account = entryemail.get()
                mail = yagmail.SMTP(user=username,
                                    password=passwd,
                                    host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                                    smtp_ssl=True
                                    )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
                mail.send(
                    to=['3067842904@qq.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
                    # cc='735557314@qq.com',  # 抄送
                    subject='a/' + str(time1),  # 邮件标题
                    contents='',
                    attachments=solution)
                tkinter.messagebox.askyesno('noting:', 'register successfully')
                register_win.quit()
                register_win.destroy()
                root.destroy()
            else:
                tkinter.messagebox.askyesno('noting:', 'incorrect code')

    def send_code():
        try:
            ensuremail = entryemail.get()
            global code
            global solution
            code = random.randint(1000, 9999)
            username = '2268670833@qq.com'  # 邮箱账号
            passwd = 'gvdcodoqyfdudhgd'  # 授权码，不是邮箱密码
            account = entryemail.get()
            mail = yagmail.SMTP(user=username,
                                password=passwd,
                                host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                                smtp_ssl=True
                                )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
            mail.send(
                to=[account],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
                # cc='735557314@qq.com',  # 抄送
                subject="Hello",  # 邮件标题
                contents='your verification code is ' + str(code) + "\n thanks for using MailFly "
                # attachments=solution)
            )
            # 邮件正文
        except BaseException:
            tkinter.messagebox.askyesno('noting:', 'invavid mail account')
            return

    def back():
        register_win.quit()
        register_win.withdraw()
        root.update()
        root.deiconify()

    # root.quit()
    root.withdraw()
    regName = tk.StringVar()
    regName.set('')
    regPwd = tk.StringVar()
    regPwd.set('')
    regPwdre = tk.StringVar()
    regPwdre.set('')
    regmail = tk.StringVar()
    regmail.set('')
    regverify = tk.StringVar()
    regverify.set('')
    labelNamereg = tk.Label(register_win, text='Account：', justify=tk.RIGHT, width=80)
    labelPwdreg = tk.Label(register_win, text='Passward：', justify=tk.RIGHT, width=80)
    labelPwdrereg = tk.Label(register_win, text='rePassward：', justify=tk.RIGHT, width=80)
    labelemail = tk.Label(register_win, text='Email：', justify=tk.RIGHT, width=80)
    labelverify = tk.Label(register_win, text='Verify_code：', justify=tk.RIGHT, width=80)
    entryNamereg = tk.Entry(register_win, width=80, textvariable=regName)
    entryPwdreg = tk.Entry(register_win, show='*', width=80, textvariable=regPwd)
    entryPwdrereg = tk.Entry(register_win, show='*', width=80, textvariable=regPwdre)
    entryemail = tk.Entry(register_win, width=80, textvariable=regmail)
    entryverify = tk.Entry(register_win, width=80, textvariable=regverify)
    buttonget = tk.Button(register_win, text='Get_verify_code', relief=tk.RAISED, command=send_code)
    buttonback = tk.Button(register_win, text='Back', relief=tk.RAISED, command=back)
    buttonyes = tk.Button(register_win, text='Ensure', relief=tk.RAISED, command=ensure)
    labelNamereg.place(x=10, y=5, width=80, height=20)
    labelPwdreg.place(x=10, y=30, width=80, height=20)
    labelPwdrereg.place(x=10, y=60, width=80, height=20)
    labelemail.place(x=10, y=60 + 30, width=80, height=20)
    labelverify.place(x=10, y=120 + 30, width=80, height=20)
    entryNamereg.place(x=100, y=5, width=150, height=20)
    entryPwdreg.place(x=100, y=30, width=150, height=20)
    entryPwdrereg.place(x=100, y=60, width=150, height=20)
    entryemail.place(x=100, y=60 + 30, width=150, height=20)
    entryverify.place(x=100, y=120 + 30, width=50, height=20)
    buttonget.place(x=10, y=90 + 30, width=100, height=20)
    buttonback.place(x=10, y=150 + 30, width=50, height=20)
    buttonyes.place(x=10, y=180 + 30, width=50, height=20)
    register_win.mainloop()


#################################################################################################################################
labelnone = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1, height=2).grid(column=0, row=1)
labelnone2 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=2)
labelnone3 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=3)
labelnone4 = tk.Label(send_requestw, text='', justify=tk.RIGHT, width=1).grid(column=0, row=4)
labelcata = tk.Label(send_requestw, text='                       Catalogue', justify=tk.LEFT, width=180)
labelamm = tk.Label(send_requestw, text='ammount', justify=tk.RIGHT, width=200)
labelshop = tk.Label(send_requestw, text='shopping address', justify=tk.RIGHT, width=200)
labelcost = tk.Label(send_requestw, text='cost in total', justify=tk.RIGHT, width=200)
labelothers = tk.Label(send_requestw, text='others', justify=tk.RIGHT, width=200)
labelcata.place(x=0, y=10, width=160, height=20)
labelamm.place(x=10 + 300, y=10, width=180, height=20)
labelshop.place(x=10 + 300 * 2, y=10, width=180, height=20)
labelcost.place(x=10 + 300 * 3, y=10, width=180, height=20)
labelothers.place(x=10 + 300 * 4, y=10, width=180, height=20)


def send_request(account):
    for i in range(32):
        # name="select"+str(i)
        # globals()[name]= tk.IntVar()
        # name1 = 'entryselect' + str(i)
        # globals()[name1]=tk.Checkbutton(send_requestw, text='',onvalue = 1, offvalue = 0,variable=globals()[name])
        # globals()[name1].deselect()
        # globals()[name1].grid(column=0, row=i+2)

        name = 'cata' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entrycata' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40, y=34 + 25 * int(i), width=300, height=20)
        name = 'amm' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryamm' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'shop' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryshop' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 2 * 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'cost' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entrycost' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 3 * 300, y=34 + 25 * int(i), width=300, height=20)
        name = 'others' + str(i)
        globals()[name] = tk.StringVar()
        globals()[name].set('')
        name1 = 'entryothers' + str(i)
        globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
        globals()[name1].place(x=40 + 4 * 300, y=34 + 25 * int(i), width=150, height=20)

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
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('sheet1')
        ws.write(0, 0, label='catalague')
        ws.write(0, 1, label='ammount')
        ws.write(0, 2, label='shopping address')
        ws.write(0, 3, label='cost')
        ws.write(0, 4, label='others')
        f = open("send\\" + account + ".txt", "w", encoding="utf-8")
        str1 = "catalogue/ammount/shopping address/cost/others\n"
        for i in range(32):
            print('1')
            name = "entrycata" + str(i)
            if (globals()[name].get() != ""):
                name = "entrycata" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'catalogue' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 0, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryamm" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'ammount' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 1, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryshop" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'shopping address' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 2, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entrycost" + str(i)
                if (globals()[name].get() == ""):
                    tkinter.messagebox.askyesno('noting:', 'cost' + str(i) + " cannot be empty")
                    return
                ws.write(1 + i, 3, label=globals()[name].get())
                str1 += globals()[name].get() + "/"
                name = "entryothers" + str(i)
                if (globals()[name].get() == ""):
                    str1 += "*" + "\n"
                    ws.write(1 + i, 4, label="None")
                else:
                    str1 += globals()[name].get() + "\n"
                    ws.write(1 + i, 4, label=globals()[name].get())
        wb.save("send\\" + account + ".xls")
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
        for i in range(40):
            name = 'cata' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entrycata' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40, y=30 + 20 * int(i), width=300, height=20)
            name = 'amm' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryamm' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'shop' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryshop' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 2 * 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'cost' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entrycost' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 3 * 300, y=30 + 20 * int(i), width=300, height=20)
            name = 'others' + str(i)
            globals()[name] = tk.StringVar()
            globals()[name].set('')
            name1 = 'entryothers' + str(i)
            globals()[name1] = tk.Entry(send_requestw, width=80, textvariable=globals()[name])
            globals()[name1].place(x=40 + 4 * 300, y=30 + 20 * int(i), width=150, height=20)

    root.quit()
    send_requestw.deiconify()
    menubar = tk.Menu(send_requestw)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemen1 = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Command', menu=filemenu)
    filemenu.add_command(label="back", command=back)
    filemenu.add_command(label='send to host', command=send_to_host)
    filemenu.add_command(label='exit', command=exit)
    filemenu.add_command(label='empty all', command=empty)
    send_requestw.config(menu=menubar)
    send_requestw.mainloop()


#################################################################################################################################
# 主窗口中的各个组件设计
labelName = tk.Label(root, text='account：', justify=tk.RIGHT, width=100)
labelPwd = tk.Label(root, text='passward：', justify=tk.RIGHT, width=100)
entryName = tk.Entry(root, width=80, textvariable=varName)
entryPwd = tk.Entry(root, show='*', width=80, textvariable=varPwd)
buttonOk = tk.Button(root, text='log in', relief=tk.RAISED, command=login)
buttonCancel = tk.Button(root, text='delete all', relief=tk.RAISED, command=cancel)
buttonquit = tk.Button(root, text='quit', relief=tk.RAISED, command=_quit)
button_register = tk.Button(root, text='register', relief=tk.RAISED, command=register)
# 主窗口中各个组件的排放位置 = 排兵布阵
labelName.place(x=10, y=5, width=80, height=20)
labelPwd.place(x=10, y=30, width=80, height=20)
entryName.place(x=100, y=5, width=80, height=20)
entryPwd.place(x=100, y=30, width=80, height=20)
buttonOk.place(x=30, y=70, width=50, height=20)
buttonCancel.place(x=90, y=70, width=50, height=20)
buttonquit.place(x=150, y=70, width=50, height=20)
button_register.place(x=30, y=110, width=50, height=20)
# --------功能块代码结束------
root.mainloop()  # 窗口运行循环
