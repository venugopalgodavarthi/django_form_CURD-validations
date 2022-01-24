from django.http import HttpResponse
from django.shortcuts import render,redirect
from customer.forms import customerform
from customer.models import customermodels
from datetime import datetime
def customerreg(request):
    form=customerform()
    if request.method=="POST":
        form=customerform(request.POST)
        if form.is_valid():
            if request.POST['password']==request.POST['repassword']:
                customermodels.objects.create(
                cname=request.POST['cname'],email=request.POST['email'],
                phone=request.POST['phone'],dob=request.POST['dob'],
                gender=request.POST['gender'],password=request.POST['password'],dor=datetime.now())
                return redirect('/cust/cselect/')
    return render(request,'cregister.html',{'form':form})

def cselect(request):
    res=customermodels.objects.all()
    return render(request,'cselect.html',{'res':res})

def cupdate(request,data):
    if request.method=="POST":
        customermodels.objects.filter(id=data).update(
                cname=request.POST['cname'],email=request.POST['email'],
                phone=request.POST['phone'],dob=request.POST['dob'],
                gender=request.POST['gender'])
        return HttpResponse('update is success')
    res=customermodels.objects.get(id=data)
    return render(request,'cupdate.html',{'res':res})

def cdelete(request,data):
    customermodels.objects.filter(id=data).delete()
    return HttpResponse('delete is success')
    
    
    
