from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from cart_app.forms import OrderForm
from cart_app.models import CartModel, OrderModel
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

    cart_items = CartModel.objects.filter(user=request.user).all()
    delivery = 5

    total_price = sum([item.total_price() for item in cart_items])
    total_products_count = sum([item.quantity for item in cart_items])

    form = OrderForm()

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)
            order.user = request.user
            order.total_products_qty = total_products_count
            order.total_price = total_price
            order.save()

            for item in cart_items:

                product = item.product
                product.quantity -= item.quantity
                product.save()
                order.items.add(item)

            cart_items.delete()
            order.save()

            return redirect('order-success')

    context = {
        'cart_items': cart_items,
        'sub_total': total_price,
        'grand_total': total_price + delivery,
        'delivery': delivery,
        'form': form
    }

    return render(request, 'cart/checkout.html', context)


@login_required(login_url='login')
def successful_order_page(request):
    return render(request, 'cart/order_success.html')


@login_required(login_url='login')
def delete_order(request, pk):

    order = OrderModel.objects.get(pk=pk)
    order.delete()
    url = reverse('profile-orders', kwargs={'pk': request.user.pk})

    return redirect(url)


@login_required(login_url='login')
def ordered_details(request, pk):

    order = OrderModel.objects.get(pk=pk)
    ordered_items = order.items.all()

    context = {
        'items': ordered_items,
        'order': order
    }

    return render(request, 'cart/order_details.html', context)




