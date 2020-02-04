import yagmail

username = '3067842904@qq.com'#邮箱账号
passwd = 'lbqwufvmzyefdeab'#授权码，不是邮箱密码
mail = yagmail.SMTP(user=username,
                    password=passwd,
                    host='smtp.qq.com',#其他服务器就smtp.qq.com  smtp.126.com
                    smtp_ssl=True
                    ) #如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
mail.send(
    to=['3067842904@qq.com'], #如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
    cc='735557314@qq.com',#抄送
    subject='test_test_test',#邮件标题
    contents='test_test_test',#邮件正文
    attachments=[r'C:\Users\qwe\Desktop\for_python\idea\product\p18402213.txt'])#附件如果只有一个的话，用字符串就行，attachments=r'C:\\pp\\b.txt'
print('发送成功')
