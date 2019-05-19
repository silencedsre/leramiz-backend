from django.shortcuts import render
from .forms import Inquire
from .models import ContactInquiry
# Create your views here.

def contact(request):
    form = Inquire(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        contact_inquire = ContactInquiry(name=name, email=email, message=message)
        contact_inquire.save()

    context = {'form':form}

    return render(request, "contact/contact.html", context=context)