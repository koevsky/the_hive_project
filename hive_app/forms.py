from django import forms


class ContactForm(forms.Form):
    your_email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.EmailInput
    )

    subject = forms.CharField(
        max_length=100,
        required=False
    )

    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

