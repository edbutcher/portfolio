from django.contrib import admin

from .forms import SignUpForm, ContactForm
from .models import SignUp, ContactMe


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)


# class ContactMeAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "timestamp", "full_name"]
#     form = ContactForm
#
#     class Meta:
#         model = ContactMe
#
admin.site.register(ContactMe)
