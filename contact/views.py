from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm


def contact(request):
    """A view to show the contact page"""

    user = request.user

    subject = "Thank you for contacting PC HAVEN"
    from_email = "pchaven.com"

    html_message = render_to_string(
        "contact/emails/contact_email.html",
    )
    plain_message = strip_tags(html_message)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            to_email = [email]
            form.save()
            messages.success(
                request,
                f"Thank you {name}, your message has been received!"
                f"We will be in touch shortly to this email address {email}.",
            )
            send_mail(
                subject,
                plain_message,
                from_email,
                to_email,
                html_message=html_message,
            )
            return redirect(reverse("home"))
        else:
            messages.error(
                request,
                "Contact failed. Please ensure the form is valid!",
            )

    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "contact/contact.html", context)
