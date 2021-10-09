import smtplib
from builtins import ValueError
from smtplib import SMTPServerDisconnected, SMTPHeloError, SMTPAuthenticationError, SMTPNotSupportedError, SMTPException


class Mailing:
    def send_contact_email(self, mail_from: str, subject: str, body: str):
        mail_user = 'myemail@mail.com'
        password = 'myS3cr3tP@ssw0rd'
        email_text = "From: " + mail_from + "\r\n" + \
                     "To: %s\r\n" % ", ".join(mail_user) + \
                     "Subject: %s\r\n" % subject + \
                     "%s" % body
        print("to: ")
        print("%s\r\n" % ", ".join(mail_user))

        print("Sending email...")

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(*mail_user, password)
            server.sendmail(from_addr=mail_from, to_addrs=mail_user, msg=email_text)
            server.close()

            print('Email sent!')
            return 'Success'
        except ValueError:
            print('Value Error')
        except SMTPServerDisconnected:
            print('SMTPServerDisconnected')
        except SMTPHeloError:
            print('SMTPHeloError')
        except SMTPAuthenticationError:
            print('SMTPAuthenticationError')
        except SMTPNotSupportedError:
            print('SMTPNotSupportedError')
        except SMTPException:
            print('SMTPException')

        return 'Something else went wrong...'
