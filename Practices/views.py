from django.shortcuts import render
from.models import Practices


def practices(request):
    practices = Practices.objects.all()
    return render(request,'practices.html',{'practices': practices})

def practices_details(request,slug):
     practice = Practices.objects.get(slug=slug)
     return render(request,'practices_detail.html',{'practice':practice})