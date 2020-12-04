import random # for create random otp num


# generating the otp # 6 digits
def otp():
    otp_num = random.randint(100000,999999)
    return otp_num


