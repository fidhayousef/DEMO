# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People


# Create your views here.
def demo(request):
    object2 = Place.objects.all()
    object1 = People.objects.all()
    return render(request, "index.html",{'value': object2,'val': object1})


    # return render(request,"index1.html")
    # name="good morning india"
    # return render(request,"index2.html",{'obj':name})
# def addition(request):
#     a=int(request.GET['num1'])
#     b=int(request.GET['num2'])
#     res=a+b
#     return render(request,"result.html",{'result':res})

# def demo(request):
#     return render(request,"index2.html")
#     # return HttpResponse("hello world")
# def about(request):
#     return render(request,"about1.html")
# def contact(request):
#     return HttpResponse("hello my contact number:9865437007")
