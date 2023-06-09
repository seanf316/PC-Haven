from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """A view to show the contact page"""

    user = request.user

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            form.save()
            messages.success(
                request,
                f"Thank you {name}, your message has been received!"
                f"We will be in touch shortly to this email address {email}.",
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
