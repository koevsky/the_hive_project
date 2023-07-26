from django import forms

from cart_app.models import Order, CartItem


class OrderForm(forms.ModelForm):

    expiration_date = forms.DateField(required=True, widget=forms.DateInput)

    class Meta:

        model = Order
        exclude = ['user', 'items', 'total_products_qty', 'total_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class EditItem(forms.ModelForm):

    class Meta:
        model = CartItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'