from django.shortcuts import render
from .models import Inquiry
from .forms import FormInquiry

def contact_form(request):
    if request.method == "POST":
        form = FormInquiry(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormInquiry()
    return render(request, 'contact.html', {'form': form})
