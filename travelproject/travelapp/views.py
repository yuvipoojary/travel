from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
   # name="Mathematics"
   obj=Place.objects.all()
   return render(request,"index.html",{'result':obj})

# def maths(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    add=x+y
#    sub=x-y
#    mult=x*y
#    div=x/y
#    return render(request,"about.html", {'resadd':add, 'ressub':sub, 'resmult':mult, 'resdiv':div})
#  {}
#
# def contact(contact):
#    return HttpResponse("contact me here")








