from django import forms

from .models import SignUp, ContactMe


class ContactForm(forms.ModelForm):

    full_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactMe
        fields = ['full_name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # write validation code.
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # write validation code.
        return full_name


class SignUpForm(forms.ModelForm):

    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # write validation code.
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # write validation code.
        return full_name
