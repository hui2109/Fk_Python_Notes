import mimetypes
import os.path
import poplib
from email.parser import BytesParser
from email.policy import default

pop3_server = 'pop.qq.com'
email = '1282798359@qq.com'
password = 'zbkltggebgpxbace'

conn = poplib.POP3_SSL(pop3_server, 995)
conn.set_debuglevel(1)
print(conn.getwelcome().decode('utf-8'))

print('--------------------')

conn.user(email)
conn.pass_(password)

message_num, total_size = conn.stat()
print('邮件数：%s，总大小：%s' % (message_num, total_size))

print('--------------------')

resp, mails, octets = conn.list()
print('响应码', resp, mails, octets)

print('--------------------')

resp2, data, octets2 = conn.retr(len(mails))
msg_data = b'\r\n'.join(data)
msg = BytesParser(policy=default).parsebytes(msg_data)
print(type(msg))
print('发件人：' + msg['from'])
print('收件人：' + msg['to'])
print('主题：' + msg['subject'])
print('第一个收件人名字：' + msg['to'].addresses[0].username)
print('第一个发件人名字：' + msg['from'].addresses[0].username)

print('--------------------')

for part in msg.walk():
    counter = 1
    if part.get_content_maintype() == 'multipart':
        continue
    elif part.get_content_maintype() == 'text':
        print(part.get_content())
    else:
        filename = part.get_filename()
        if not filename:
            ext = mimetypes.guess_extension(part.get_content_type())
            if not ext:
                ext = '.bin'
            filename = 'part-%03d%s' % (counter, ext)
        counter += 1
        with open(os.path.join('.', filename), 'wb') as fp:
            fp.write(part.get_payload(decode=True))
conn.quit()
