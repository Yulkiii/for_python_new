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
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()
