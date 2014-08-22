# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = 'hello world'

msg['Subject'] = 'new message'
msg['From'] = ***
msg['To'] = ***

s = smtplib.SMTP('smtp.gmail.com')
s.sendmail(me, [you], msg.as_string())
s.quit()