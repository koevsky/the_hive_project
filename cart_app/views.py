from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cart_app.models import CartModel
from product_app.models import ProductModel


@login_required(login_url='login')
def cart_view(request):

    cart_items = CartModel.objects.filter(user=request.user)
    context = {'cart_items': cart_items}

    return render(request, 'cart/cart_details.html', context)


@login_required(login_url='login')
def add_to_cart(request, pk):

    product = ProductModel.objects.get(pk=pk)
    cart_item = CartModel.objects.create(user=request.user, product=product)
    cart_item.save()

    return redirect('shop')


@login_required(login_url='login')
def remove_from_cart(request, pk):

    product = ProductModel.objects.get(pk=pk)
    cart_item = CartModel.objects.filter(user=request.user, product=product)
    cart_item.delete()

    return redirect('cart-details')


