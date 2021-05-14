from django.urls import path
from . import views

app_name="buyer"

urlpatterns = [
	path('home/', views.home),
	path('cart/<int:id>/', views.cart, name="cart"),
	path('cartdetails/', views.cartdetails),
	path('cartcalculate/', views.cartcalculate),
]