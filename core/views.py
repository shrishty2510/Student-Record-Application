from django.shortcuts import render ,HttpResponseRedirect
from django.contrib import messages
from datetime import date, time ,datetime
from . models import Student
from . forms import Studentinfo

def studentadd(request):
    if request.method == 'POST':
       form=Studentinfo(request.POST)
       if form.is_valid():
           data=form.cleaned_data
           nm= data['name']
           em= data['email']
           pw= data['password']
           st= data['standard']
           #da= data['date']
           reg = Student(name=nm,standard=st,email=em,password=pw,date= datetime.today())
           reg.save()
           messages.success(request,'Added Sucessfully !!')
           form=Studentinfo()
           #form.save()
    else:   
        form=Studentinfo()
    stud=Student.objects.all()
    return render(request,'core/home.html',{'fr':form,'stu':stud})

def studentupdate(request,id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id,)    
        form=Studentinfo(request.POST,instance=pi)
        if form.is_valid():
           form.save()
           messages.success(request,"Updated Successfully !!")
    else:
           pi = Student.objects.get(pk=id,)    
           form=Studentinfo(instance=pi)
    return render(request,'core/review.html',{'fr':form})   
           
    
def delete_data(request,id):
    if request.method == 'POST':
       pi = Student.objects.get(pk=id)
       pi.delete()
       messages.success(request,"Deleted Successfully !!")
       return HttpResponseRedirect('/')


# Create your views here.
