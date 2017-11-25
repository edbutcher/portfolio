from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm, SignUpForm


def home(request):

    return render(request, "home.html")


def contact(request):
    title = "Or message me"
    form = ContactForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        form.save()
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]     # a list of emails

        contact_message = "%s: %s via %s" % (form_full_name, form_message, form_email)

        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            fail_silently=True,
        )

        context = {
            "form": form,
            "title": "Thanks for sending message!*"
        }

    return render(request, "contact.html", context)
