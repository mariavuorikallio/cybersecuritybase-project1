from django.urls import path
from . import views

urlpatterns = [
    path("", views.productListView, name="product"),
    path("products/<int:pid>/", views.productDetailView, name="product_detail"),
    path("cart/<int:pid>/", views.addToCartView, name="cart"),
    path("cart/view/", views.viewCart, name="view_cart"), 
    path("checkout/", views.checkoutView, name="checkout"), 
    path('checkout/place_order/', views.placeOrderView, name='place_order'),
    path("search/", views.searchProduct, name="search"),
]
