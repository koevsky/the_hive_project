from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages


from cart_app.models import CartModel
from product_app.models import ProductModel


@login_required(login_url='login')
def cart_view(request):

    cart_items = CartModel.objects.filter(user=request.user).order_by('created_at')
    total_money = sum([item.quantity * item.product.price for item in cart_items])
    context = {
        'cart_items': cart_items,
        'total_money': total_money,
    }

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


@login_required(login_url='login')
def update_cart(request, pk):

    item = CartModel.objects.get(pk=pk)
    new_quantity = int(request.POST.get(f'quantity_{item.pk}', 0))

    if new_quantity > item.product.quantity or new_quantity < 0:

        error_message = f"Error - invalid input!"
        cart_items = CartModel.objects.filter(user=request.user).order_by('created_at')
        total_money = sum([item.quantity * item.product.price for item in cart_items])

        context = {
            'error_message': error_message,
            'cart_items': cart_items,
            'total_money': total_money
        }

        return render(request, 'cart/cart_details.html', context)

    item.quantity = new_quantity
    item.save()

    return redirect('cart-details')


@login_required(login_url='login')
def checkout_page(request):

    cart_items = CartModel.objects.filter(user=request.user)
    total = sum([item.total_price() for item in cart_items])
    delivery = 5

    context = {
        'cart_items': cart_items,
        'grand_total': total,
        'delivery': delivery
    }
    return render(request, 'cart/checkout.html', context)
