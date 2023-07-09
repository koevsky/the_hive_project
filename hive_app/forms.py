from django import forms


class ContactForm(forms.Form):

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your email [required]',
                'class': 'form-control'
            }
        )
    )

    subject = forms.CharField(
        required=True,
        max_length=200,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject [required]',
                'class': 'form-control'
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message',
                'class': 'form-control'
            }
        )
    )

