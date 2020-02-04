from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
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
                    value = u'%s <%s>' % (name, addr)
            #print('%s%s:%s' % ('  ' * indent, header, value))
            print("%s",value)
def get_att(msg):
    attachment_files = []
    for part in msg.walk():
        file_name = part.get_filename()  # 获取附件名称类型
        contType = part.get_content_type()
        if file_name:
            print(file_name)
            filename=file_name
            '''
            dh = email.header.decode_header(h)  # 对附件名称进行解码
            filename = dh[0][0]
            if dh[0][1]:
                filename = decode_str(str(filename, dh[0][1]))  # 将附件名称可读化
                print(filename)
                #filename = filename.encode("utf-8")
            '''
            data = part.get_payload(decode=True)  # 下载附件
            att_file = open('C:\\Users\\qwe\\Desktop\\for_python\\file\\' + filename, 'wb')  # 在指定目录下创建文件，注意二进制文件需要用wb模式打开
            attachment_files.append(filename)
            att_file.write(data)  # 保存附件
            att_file.close()
    return attachment_files
email ='3067842904@qq.com'
password = 'lbqwufvmzyefdeab'
pop3_server='pop.qq.com'
server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
#print(server.getwelcome().decode('utf-8'))
server.user(email)
server.pass_(password)
#print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
#print(mails)# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print_info(msg)
get_att(msg)
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
