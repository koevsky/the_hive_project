def cart_items_processor(request):
    if request.user.is_authenticated:

        items = request.user.cartmodel_set.all()

    else:

        items = []

    total_items_price = sum(item.product.price * item.quantity for item in items)

    return {
        'items': items,
        'total_items_price': total_items_price
    }