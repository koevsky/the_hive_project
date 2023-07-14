from django import forms

from apiary_app.models import ApiaryModel
from product_app.models import ProductModel


class ProductForm(forms.ModelForm):

    apiary = forms.ModelChoiceField(queryset=None)

    class Meta:

        model = ProductModel
        exclude = ['owner']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['apiary'].queryset = ApiaryModel.objects.filter(owner=user)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DeleteProductForm(ProductForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True