import poplib
import email
import time
from email.parser import Parser
from email.header import decode_header


def decode_str(s):#字符编码转换
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def get_att(msg):
    attachment_files = []
    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        contType = part.get_content_type()
        if file_name:
            h = email.header.Header(file_name)
            dh = email.header.decode_header(h)  # 对附件名称进行解码
            filename = dh[0][0]
            if dh[0][1]:
                filename = decode_str(str(filename, dh[0][1]))  # 将附件名称可读化
                print(filename)
                #filename = filename.encode("utf-8")
            data = part.get_payload(decode=True)  # 下载附件
            att_file = open('C:\\Users\\qwe\\Desktop\\for_python\\file\\' + filename, 'wb')  # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    return attachment_files


'''
with open('D:\\config.txt', 'r') as f1:
    config = f1.readlines()
for i in range(0, len(config)):
    config[i] = config[i].rstrip('\n')
'''
# print(config)

# POP3服务器、用户名、密码
host = 'pop.qq.com' # pop.163.com
username = '3067842904@qq.com'  # 用户名 
password = 'lbqwufvmzyefdeab'# 密码
# 连接到POP3服务器
server = poplib.POP3(host)

# 身份验证
server.user(username)
server.pass_(password)

#stat()#返回邮件数量和占用空间:
#print('Messages: %s. Size: %s' % server.stat())

# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
resp, mails, octets = server.list()
#print(resp)

#倒序遍历邮件
index = len(mails)
for i in range(index, 0, -1):
    # lines存储了邮件的原始文本的每一行
    resp, lines, octets = server.retr(i)
    # 邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 解析邮件:
    msg = Parser().parsestr(msg_content)
    print(msg)
    # 获取附件
    f_list = get_att(msg)

print("文件已下载完成，10秒后关闭程序！")
time.sleep(10)
