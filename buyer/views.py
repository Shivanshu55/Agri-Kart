from django.shortcuts import render, redirect
from django.http import HttpResponse
from seller.models import Product, Category
from AgriKart.models import UserProfile
from django.core.mail import send_mail
from .models import Cart
from django.db import connection

myCursor = connection.cursor()

# Create your views here.
def home(request):
	pObjs = Product.objects.all()
	catObjs = Category.objects.all()
	uObj = UserProfile.objects.get(user__username=request.user)

	myCursor.execute("select count(*) from buyer_cart where user_id={}".format(uObj.id))
	res = myCursor.fetchone()

	return render(request, "WelcomeBuyer.html", {'products' : pObjs, 'catObjs':catObjs, 'count' : res[0]})

def cart(request, id):
	pObj = Product.objects.get(id=id)
	uObj = UserProfile.objects.get(user__username=request.user)

	url = '/buyer/home/'
	try:
		c = Cart(product=pObj, user=uObj)
		c.save()
	except:
		return HttpResponse('<script>alert("Product is already in your cart");\
			window.location="{}"</script>'.format(url))

	return HttpResponse('<script>alert("Product has been added in your cart!");\
			window.location="{}"</script>'.format(url))

	return redirect('/buyer/home/')


def cartdetails(request):

	uObj = UserProfile.objects.get(user__username=request.user)
	cartObjs = Cart.objects.filter(user_id=uObj.id)

	#print(uObj)
	#print(cartObjs)
	proItems = []

	for i in cartObjs:
		proItems.append(Product.objects.get(id=i.product_id))

	return render(request, "cart_details.html", {'added_products' : proItems})

def cartcalculate(request):
	q = request.POST.getlist('product_qty')
	price = request.POST.getlist('price')
	pid = request.POST.getlist('pid')

	uObj = UserProfile.objects.get(user__username=request.user)
	#print(q, price, pid)
	total = 0
	for i in range(len(q)):
		total = total + int(q[i]) * float(price[i])

		#Updating Product Stock
		updatePro = Product.objects.filter(id=pid[i])
		updatedQty = int(updatePro[0].qty) - int(q[i])
		updatePro.update(qty=updatedQty)

	cartObjs = Cart.objects.filter(user_id=uObj.id)
	cartObjs.delete()
	#send_mail()
	return render(request, "checkout.html", {'billAmount' : total})
