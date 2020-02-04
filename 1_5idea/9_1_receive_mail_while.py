from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
import tkinter as tk
import tkinter.messagebox
import yagmail
import random
import time
import hashlib
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
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    #value = u'%s <%s>'name, addr)
            print("%s",value)
def get_mail_name(msg):
    for header in [ 'Subject']:
            value = msg.get(header, '')
            return value
def get_att(msg,path="file\\"):
    attachment_files = []
    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        contType = part.get_content_type()
        if file_name:
            print(file_name)
            filename=file_name
            data = part.get_payload(decode=True)  # 下载附件
            att_file = open(path + filename, 'wb')  # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    return attachment_files
def check_mail_name(name_split):
    f = open("time.txt", "r", encoding="utf-8")
    time=f.read()
    time=time.split("\n")
    f.close
    try:
        if int(name_split[1]>time[0]):
            new_time=name_split[1]+"\n"+name_split[2]+"\n"+name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        if int(name_split[2]>time[1]):
            new_time=name_split[1]+"\n"+name_split[2]+"\n"+name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        if int(name_split[3]>time[2]):
            new_time=name_split[1]+"\n"+name_split[2]+"\n"+name_split[3]
            f = open("time.txt", "w", encoding="utf-8")
            f.write(new_time)
            f.close()
            return 1
        return 0
    except BaseException:
        return 0
def check_psw(account,pwd):
    try:
        file_name="file\\"+account
        f = open(file_name, "r", encoding="utf-8")
        read_in=f.read()
        read_in=read_in.split("\n")
        if(read_in[1]==pwd):
            return 1
        return 0
    except BaseException:
        return -1
def send_mail(type_of,attachment):
    time1 = time.strftime('%Y/%m%d/%H%M%S', time.localtime(time.time()))
    username = '3067842904@qq.com'  # 邮箱账号
    passwd = 'lbqwufvmzyefdeab'  # 授权码，不是邮箱密码
    mail = yagmail.SMTP(user=username,
                        password=passwd,
                        host='smtp.qq.com',  # 其他服务器就smtp.qq.com  smtp.126.com
                        smtp_ssl=True
                        )  # 如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
    mail.send(
        to=['2268670833@qq.com'],  # 如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
        # cc='735557314@qq.com',  # 抄送
        subject=type_of+'/' + str(time1),contents='' , attachments=attachment)

email ='3067842904@qq.com'
password = 'lbqwufvmzyefdeab'
pop3_server='pop.qq.com'
server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
server.user(email)
server.pass_(password)
while True:
    server = poplib.POP3(pop3_server)
    server.set_debuglevel(1)
    server.user(email)
    server.pass_(password)
    resp, mails, octets = server.list()
    index = len(mails)
    resp, lines, octets = server.retr(index)
    
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    
    msg = Parser().parsestr(msg_content)
    mail_name=get_mail_name(msg)
    mail_name_split=mail_name.split('/')
    print(mail_name_split)
    if check_mail_name(mail_name_split):
        if(mail_name_split[0]=="a"):
            get_att(msg)
        elif (mail_name_split[0]=="b"):
            get_att(msg,"file2\\")
            for part in msg.walk():
                file_name = part.get_filename()
                if file_name:
                    f = open("file2\\"+file_name, "r", encoding="utf-8")
                    read=f.read()
                    read=read.split("\n")
                    f.close()
                    result=check_psw(file_name,read[1])
                    f = open("result\\"+file_name, "w", encoding="utf-8")
                    f.write(str(result))
                    f.close()
                    send_mail("c","result\\"+file_name)
        elif (mail_name_split[0]=="c"):
            file_name=get_att(msg,"task\\")
            print(file_name)
            break
        elif(mail_name_split[0]=="t"):#teacher request
            try:
                file_name=get_att(msg,"teacherRequest\\")
                send_mail("d","task\\"+file_name)#send to teacher
            except BaseException:
                f = open("0.txt", "w", encoding="utf-8")
                f.close()
                send_mail("d","0.txt")




            
                    
server.quit()




