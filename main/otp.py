import random # for create random otp num
import yagmail


# generating the otp # 6 digits
def otp():
    otp_num = random.randint(100000,999999)
    return otp_num


def send_mail(reciever):
    otp_num = str(otp())
    yagmail.register('Ebazaar.web@gmail.com', '###pasword fro the email id')
    receiver = reciever
    body = "your otp is: "+otp_num

    yag = yagmail.SMTP("Ebazaar.web@gmail.com")
    yag.send(
        to=receiver,
        subject="Ebazaar otp",
        contents=body, 
    )
    return otp_num

