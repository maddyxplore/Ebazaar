from django.shortcuts import render
from . import otp
import yagmail

global otp_secret
otp_secret = otp.otp()

# sending email
def send_mail(reciever):
    otp_num = str(otp_secret)
    yagmail.register('Ebazaar.web@gmail.com', 'madman2018')
    receiver = reciever
    body = "your otp is: "+otp_num

    yag = yagmail.SMTP("Ebazaar.web@gmail.com")
    yag.send(
        to=receiver,
        subject="Ebazaar otp",
        contents=body, 
    )

def login(request):
   return render(request, "login.html")

def signuppath(request):
   return render(request, "signuppath.html")

def fsignup(request):
   return render(request, "fsignup.html")


def csignup(request):
   return render(request, "csignup.html")


def verify(request):
   if request.method == "POST":
      email = request.POST["email"]
      send_mail(email)
      data_set = {"email":email}
      return render(request, "verify.html",{'data_set':data_set})
   elif request.method == "GET":
      otp_num = request.GET["otp"]
      email = request.GET["email"]
      print("otp",type(otp_secret))
      print(type(otp_num))
      if str(otp_secret) == otp_num:
         return render(request, "login.html")
      else:
         return render(request, "signup.html")

