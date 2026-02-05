from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product

def productListView(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

def productDetailView(request, pid):
    product = Product.objects.get(id=pid)
    request.session['user'] = pid
    return render(request, 'marketplace/product_detail.html', {'product': product})

def addToCartView(request, pid):
    # FLAW 1: State-changing operation is performed via GET request
    # without CSRF protection. An attacker can add items to the user's
    # cart by forcing the browser to load /marketplace/cart/<pid>/.

    cart = request.session.get('cart', [])
    cart.append(pid)
    request.session['cart'] = cart
    return redirect('view_cart')

    # FIX (commented out):
    # from django.views.decorators.http import require_POST
    #
    # @require_POST
    # def addToCartView(request, pid):
    #     cart = request.session.get('cart', [])
    #     if pid not in cart:
    #         cart.append(pid)
    #     request.session['cart'] = cart
    #     return redirect('view_cart')

def viewCart(request):
    cart_ids = request.session.get('cart', [])
    print("Cart session contents:", cart_ids)  # <--- FLAW 3: Sensitive data is logged

    cart_items = Product.objects.filter(id__in=cart_ids)
    return render(request, 'marketplace/cart.html', {'cart': cart_items})

# FIX (commented out):
# def viewCart(request):
#     cart_ids = request.session.get('cart', [])
#     # Do not log sensitive session data in production
#     # print("Cart session contents:", cart_ids)
#     cart_items = Product.objects.filter(id__in=cart_ids)
#     return render(request, 'marketplace/cart.html', {'cart': cart_items})

# FLAW 5: Broken Authentication / Authorization – checkout accessible without login
def checkoutView(request):
    cart_ids = request.session.get('cart', [])
    cart_items = Product.objects.filter(id__in=cart_ids)
    total_price = sum(item.price for item in cart_items)
    return render(request, 'marketplace/checkout.html', {'cart': cart_items, 'total': total_price})

# FIX (commented out):
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def checkoutView(request):
#     cart_ids = request.session.get('cart', [])
#     cart_items = Product.objects.filter(id__in=cart_ids)
#     total_price = sum(item.price for item in cart_items)
#     return render(request, 'marketplace/checkout.html', {'cart': cart_items, 'total': total_price})

def placeOrderView(request):
    request.session['cart'] = []
    return render(request, 'marketplace/order_success.html')

def searchProduct(request):
    query = request.GET.get("q", "")
    # FLAW 4: SQL Injection – user input is directly used in a raw SQL query
    products = Product.objects.raw(
        f"SELECT * FROM marketplace_product WHERE name LIKE '%{query}%'"
    )
    return render(request, "marketplace/product_list.html", {"products": products})

# FIX (commented out):
# def searchProduct(request):
#     query = request.GET.get("q", "")
#     # Use Django ORM to safely filter products and prevent SQL Injection
#     products = Product.objects.filter(name__icontains=query)
#     return render(request, "marketplace/product_list.html", {"products": products})

