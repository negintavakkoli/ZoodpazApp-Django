from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect





def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, template_name = "index.html")

# Create your views here.

def readata(request):
    grocery = request.POST.get("grocery", "")
    check = 0
    if request.POST.get("checkbox-1", ""):
        check = 1
    print(grocery)
    print(check)
    context = {"check":check,
           "grocery":grocery}
    return render(request, template_name = "index.html", context=context)

