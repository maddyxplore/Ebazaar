from django.shortcuts import render
from django.contrib.auth.models import auth
from .models import User,cuser,fuser
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
   if request.method == 'POST':
      name = request.POST['username']
      name = User.objects.get(email=name.lower()).username
      password = request.POST['password']
      user = auth.authenticate(username=name , password = password)
      data_set = {user:"customer"}
      return render(request,"logged.html",{'data_set':data_set})      
   else:
      return render(request, "login.html")

def signuppath(request):
   return render(request, "signuppath.html")

def fsignup(request):
   return render(request, "fsignup.html")


def csignup(request):
   return render(request, "csignup.html")


def cverify(request):
   if request.method == "POST":
      first_name = request.POST["first_name"]
      second_name = request.POST["second_name"]
      user_name = request.POST["user_name"]
      email = request.POST["email"]
      phone = request.POST["phone"]
      password = request.POST["password"]
      location = request.POST["location"]
      address = request.POST["address"].replace(" ","")
      # sending email
      send_mail(email)
      # data set to otp verification 
      data_set = {"first_name":first_name,"second_name":second_name,"user_name":user_name,"phone":phone,"password":password,"location":location,"address":address,"email":email}

      return render(request, "cverify.html",{'data_set':data_set})

   elif request.method == "GET":
      first_name = request.GET["first_name"]
      second_name = request.GET["second_name"]
      user_name = request.GET["user_name"]
      email = request.GET["email"]
      phone = request.GET["phone"]
      password = request.GET["password"]
      location = request.GET["location"]
      address = request.GET["address"]
      otp_num = request.GET["otp"]
      shop_no = ""
      if str(otp_secret) == otp_num:
         temp_user = User.objects.create_user(first_name = first_name , last_name = second_name , username = user_name, password = password , email = email , is_staff = False)
         user = cuser(Phone=phone,Location=location,Address=address,user=temp_user)
         user.save()
         return render(request, "login.html")
      else:
         return render(request, "csignup.html")

def fverify(request):
   if request.method == "POST":
      first_name = request.POST["first_name"]
      second_name = request.POST["second_name"]
      user_name = request.POST["user_name"]
      email = request.POST["email"]
      phone = request.POST["phone"]
      password = request.POST["password"]
      location = request.POST["location"]
      shop_no = request.POST["shop_no"]
      # sending email
      send_mail(email)
      # data set to otp verification 
      data_set = {"first_name":first_name,"second_name":second_name,"phone":phone,"password":password,"location":location,"shop_no":shop_no,"email":email}

      return render(request, "fverify.html",{'data_set':data_set})
   
   elif request.method == "GET":
      first_name = request.GET["first_name"]
      second_name = request.GET["second_name"]
      user_name = request.GET["user_name"]
      email = request.GET["email"]
      phone = request.GET["phone"]
      password = request.GET["password"]
      location = request.GET["location"]
      shop_no = request.GET["shop_no"]
      otp_num = request.GET["otp"]

      if str(otp_secret) == otp_num:
         temp_user = User.objects.create_user(first_name = first_name , last_name = second_name , username = user_name, password = password , email = email , is_staff = True)
         user = fuser(Phone=phone,Location=location,Shop_no=shop_no,user=temp_user)
         user.save()
         return render(request, "login.html")
      else:
         return render(request, "fsignup.html")
