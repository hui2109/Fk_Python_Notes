import smtplib
from email.message import EmailMessage

smtp_server = 'smtp.qq.com'
from_addr = '995631664@qq.com'
password = 'rqjwtvbfrhdybdjf'
to_addr = '1282798359@qq.com'

conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)

msg = EmailMessage()
msg.set_content(
    '<h2>邮件内容</h2>' + '<p>您好，这是一封来自Python的邮件<p>' + '来自<a href="https://www.crazyit.org">疯狂联盟</a>',
    'html', 'utf-8')
msg['subject'] = '一封HTML邮件'
msg['from'] = '张旭辉 <%s>' % from_addr
msg['to'] = '辉哥小号 <%s>' % to_addr

conn.sendmail(from_addr, [to_addr], msg.as_string())
conn.quit()
