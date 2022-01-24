from django.shortcuts import render
from student.forms import registerForm
# Create your views here.
def registerview(request):
    form=registerForm()
    print(form)
    return render(request,'register.html',{'form':form})
