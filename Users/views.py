from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.db.utils import IntegrityError
from .forms import Registration


# Create your views here.
def signup(request):
    if request.method ==  'POST':
        form = Registration(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request,'about_us1.html')
            except:
                return render(request,'Error.html')
        else:
            return render(request,'Error.html')
    else:
        form = Registration()
        return render(request, 'signupage.html',{'form' : form})
