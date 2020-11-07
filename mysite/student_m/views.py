from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import student
# Create your views here.
def home(request):
    return render(request,'home.html')

def student_form(request, id=0):

    if request.method == 'GET':
        if id==0:
            form =  StudentForm()
        else:
            print("get id ",id)
            std = student.objects.get(pk=id)
            # print(std.present )
            form = StudentForm(instance=std)
            print(std.present)
            std.present+=1
            print(std.present)
            std.save()
            return redirect('/student/list/')
        return render(request,'student_form.html',{'form':form})
    else:
        if id == 0:
            print("id==0")
            form =  StudentForm(request.POST)
        else:
            print("id",id)
            std = student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=std)

        if form.is_valid():
            form.save()
        return redirect('/student/list/')

def student_list(request):
    context =  student.objects.all()
    return render(request,'student_list.html',{'context':context})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request,user)
            print("hello")
            #if form get saved
            return render(request,'home.html')
    print("this")
    form = UserCreationForm()
    return render(request,'signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       print("hi")
       if form.is_valid():
           print("log in user")
           user = form.get_user()
           login(request,user)
           return render(request,'home.html')

    else:
        print("no posting")
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})