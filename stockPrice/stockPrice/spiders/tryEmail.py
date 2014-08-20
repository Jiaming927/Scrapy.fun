from scrapy.mail import MailSender
mailer = MailSender()

mailer.send(to=["jiaminguw@gmail.com"], subject="This is the subject", body="HELLO WORLD")