from django.shortcuts import render, redirect
from .models import Category, Product
from AgriKart.models import UserProfile

# Create your views here.
def home(request):
	return render(request, "WelcomeSeller.html")

def add_product(request):
	catObjs = Category.objects.all()

	if request.method == "POST":
		pname = request.POST['pname']
		price = request.POST['price']
		qty = request.POST['qty']
		desc = request.POST['desc']
		pic = request.FILES['pic']
		catid = request.POST['catid']

		uObj = UserProfile.objects.get(user__username=request.user)
		catObj = Category.objects.get(id=catid)

		p = Product(pname=pname, price=price, qty=qty, desc=desc, pic=pic, category=catObj, added_by=uObj)
		p.save()
		return redirect("/seller/add_product/")



	return render(request, 'add_product.html', {'data' : catObjs})
