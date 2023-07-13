from django import forms

from apiary_app.models import ApiaryModel


class ApiaryForm(forms.ModelForm):

    class Meta:
        model = ApiaryModel
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ApiaryDeleteForm(ApiaryForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


