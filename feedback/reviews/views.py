from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from .models import Review

def review(request):
    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thank-you')
    else:
        form=ReviewForm()
    
    return render(request,"review.html",{
        "form":form
    })

def thanks(request):
    return render(request,'thanku.html')