from django.shortcuts import render
from . import otp


num = otp.send_mail("madhansubramani20022000@gmail.com")
print(num)

def login(request):
   return render(request, "login.html")

def signup(request):
   return render(request, "signup.html")

def verify(request):
   name = request.POST["name"]    

   
   return render(request, "verify.html")