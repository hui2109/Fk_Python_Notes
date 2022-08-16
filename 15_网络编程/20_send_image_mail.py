import email.utils
import smtplib
from email.message import EmailMessage
import os

os.chdir(os.path.dirname(__file__))

smtp_server = 'smtp.qq.com'
from_addr = '995631664@qq.com'
password = 'rqjwtvbfrhdybdjf'
to_addr = '1282798359@qq.com'

conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)

msg = EmailMessage()
first_id, second_id = email.utils.make_msgid(), email.utils.make_msgid()
msg.set_content('<h2>邮件内容</h2>' +
                '<p>您好，这是一封来自Python的邮件' +
                '<img src="cid:' + second_id[1:-1] + '"><p>' +
                '来自<a href="https://www.crazyit.org">疯狂联盟</a>' +
                '<img src="cid:' + first_id[1:-1] + '">', 'html', 'utf-8')
msg['subject'] = '另一封带图片的HTML邮件'
msg['from'] = '张旭辉 <%s>' % from_addr
msg['to'] = '辉哥小号 <%s>' % to_addr

with open('路飞.jpeg', 'rb') as f1:
    msg.add_attachment(f1.read(), maintype='image', subtype='jpeg', filename='test1.jpeg', cid=first_id)
with open('乔巴.jpeg', 'rb') as f2:
    msg.add_attachment(f2.read(), maintype='image', subtype='jpeg', filename='test2.jpeg', cid=second_id)
with open('泡型肝包虫病的超声诊断再探讨—附100例分析.pdf', 'rb') as f3:
    msg.add_attachment(f3.read(), maintype='application', subtype='pdf', filename='test3.pdf')
conn.sendmail(from_addr, [to_addr], msg.as_string())
conn.quit()
