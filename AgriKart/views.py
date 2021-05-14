from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

def home(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == "POST":
		fname = request.POST['fname']
		lname = request.POST['lname']
		uname = request.POST['uname']
		pwd = request.POST['pwd']
		email = request.POST['email']
		mob = request.POST['mob']
		utype = request.POST['utype']


		u = User(first_name=fname, last_name=lname, username=uname, password=make_password(pwd), email=email)
		u.save()

		up = UserProfile(user=u, mobile=mob, usertype=utype)
		up.save()
		return redirect('/signup/')


	return render(request, "signup.html")

def login_call(request):
	if request.method == "POST":
		uname = request.POST['uname']
		pwd = request.POST['pwd']

		selUser = authenticate(username=uname, password=pwd)
		print(selUser)
		print(type(selUser))

		if selUser:
			login(request, selUser)
			uObj = UserProfile.objects.get(user__username=request.user)
			#print(request.user)
			#select usertype from ecommerceproject_userprofile where user_id=(select id from auth_user where username='vijay123')
			if uObj.usertype == "buyer":
				return redirect('/buyer/home/')
			elif uObj.usertype == "seller":
				return redirect('/seller/home/')

		else:
			return HttpResponse("Invalid Login Details!")


	return render(request, "login.html")

def logout_call(request):
	logout(request)
	return redirect('/home/')
