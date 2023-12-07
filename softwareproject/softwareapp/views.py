from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Waterfalls

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob = Waterfalls.objects.all()

    return render(request,"index.html",{'result':obj,'rslt':ob})

#def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    return render(request,"result.html",{'result':res})

#def demo(request):
 #   return  render(request,"home.html")

#def about(request):
#    return render(request,"result.html")

#def contact(request):
#    return HttpResponse("hello am contact")