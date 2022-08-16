import smtplib
from email.message import EmailMessage

smtp_server = 'smtp.qq.com'
from_addr = '995631664@qq.com'
password = 'rqjwtvbfrhdybdjf'
to_addr = '1282798359@qq.com'

# conn=smtplib.SMTP(smtp_server,25)
conn = smtplib.SMTP_SSL(smtp_server, 465)
conn.set_debuglevel(1)
conn.login(from_addr, password)

msg = EmailMessage()
msg.set_content('您好，这是一封来自Python的邮件', 'plain', 'utf-8')
conn.sendmail(from_addr, [to_addr], msg.as_string())
conn.quit()
