from cart_app.models import Cart


def cart_items_processor(request):

    if request.user.is_authenticated:

        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()

    else:

        items = []

    if items:
        total_items_price = sum(item.item_price() for item in items)
    else:
        total_items_price = 0

    return {
        'items': items,
        'total_items_price': total_items_price
    }
