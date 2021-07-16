from _typeshed import SupportsDivMod
# from smtplib
from smtplib import SMTPException
import smtplib
from typing_extensions import final
import warnings
import logging
from email.mime.text import MIMEText


html = """\
<html>
<head>
    <body>
        <p>
            Hello bla bla bla {something}
        </p>
    </body>
</head>

</html>
""".format(something='something')

msg = MIMEText(html, 'html')
msg['subject'] = 'test message from python script'
from_email = "shubhamdeprojects@gmail.com"
# to_email =  ["shubhamdeprojects@gmail.com", "otheremail@gmail.com"]
to_email =  ["shubhamdeprojects@gmail.com"]


try : 
    smtpObj = smtplib.SMTP('mail.company.com')
    smtpObj.sendmail(from_addr=from_email, to_addrs=to_email)
except SMTPException:
    raise Exception("Error while sending the email")
finally:
    smtpObj.close()