from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from cart_app.forms import OrderForm
from cart_app.models import Cart, CartItem, Order

from product_app.models import ProductModel
from the_hive_core.decorators import group_required


@login_required(login_url='login')
def cart_view(request):

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    context = {
        'cart_items': cart_items,
        'total_price': cart.total_price()
    }

    return render(request, 'cart/cart_details.html', context)


@login_required(login_url='login')
def add_to_cart(request, pk):

    product = ProductModel.objects.get(pk=pk)
    cart = Cart.objects.get(user=request.user)

    cart_item = cart.items.filter(product_id=pk).first()

    if cart_item in cart.items.all():

        cart_item.quantity += 1
        cart_item.save()

    else:

        cart_item = CartItem.objects.create(product=product)
        cart.items.add(cart_item)

    cart.save()

    previous_page = request.META.get('HTTP_REFERER')

    return redirect(previous_page)


@login_required(login_url='login')
def remove_from_cart(request, pk):

    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()

    return redirect('cart-details')


@login_required(login_url='login')
def update_cart(request, pk):

    item = CartItem.objects.get(pk=pk)
    product_qty = item.product.quantity
    new_quantity = int(request.POST.get(f'quantity_{item.pk}', 0))

    if new_quantity == 0:
        item.delete()

    if new_quantity > product_qty or new_quantity < 0:

        error_message = f"Error - invalid input!"
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        total_money = cart.total_price()

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

    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    total_qty = sum(item.quantity for item in cart_items)
    delivery = 5

    form = OrderForm()

    if request.method == 'POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user
            order.total_price = cart.total_price() + delivery
            order.total_products_qty = total_qty
            order.save()

            for item in cart_items:

                product = item.product
                product.quantity -= item.quantity
                product.save()

                order_item = CartItem.objects.create(product=product, quantity=item.quantity)
                order.items.add(order_item)

            order.save()
            cart_items.delete()

            return redirect('order-success')

    context = {
        'cart_items': cart_items,
        'sub_total': cart.total_price(),
        'grand_total': cart.total_price() + delivery,
        'delivery': delivery,
        'form': form
    }

    return render(request, 'cart/checkout.html', context)


@login_required(login_url='login')
def successful_order_page(request):
    return render(request, 'cart/order_success.html')


@login_required(login_url='login')
def delete_order(request, pk):

    order = Order.objects.get(pk=pk)
    order.delete()
    url = reverse('profile-orders', kwargs={'pk': request.user.pk})

    return redirect(url)


@login_required(login_url='login')
def order_details(request, pk):

    order = Order.objects.get(pk=pk)
    order_items = order.items.all()

    context = {
        'order_items': order_items,
        'order': order
    }

    return render(request, 'cart/order_details.html', context)