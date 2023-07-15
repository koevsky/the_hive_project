from django import forms

from hive_app.models import EmailModel


class ContactForm(forms.ModelForm):

    class Meta:
        model = EmailModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


