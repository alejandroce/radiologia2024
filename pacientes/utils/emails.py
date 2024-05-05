import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from settings.base import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_HOST_PASSWORD


def send_simple_email(subject='', message='', from_address='Radiologia<mcalejandrocontreras@gmail.com>', to_address=[]):
    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

        msg = MIMEMultipart()

        if type(to_address) == list:
            to_address = ', '.join(to_address)

        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        return 0
    except Exception as err:
        return 1