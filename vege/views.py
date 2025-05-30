from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
# Create your views here.
@login_required(login_url="/login/")
def recipies(request):
    if request.method == "POST":
 
        
        
        Recipie.objects.create(
            r_name=request.POST.get('r_name'),
            r_des=request.POST.get('r_des'),
            r_image=request.FILES.get('recipe_image')  # Matches form field name
        )
        return redirect('/recipies/')
    
    queryset = Recipie.objects.all()
    context = {'recipies': queryset}
    return render(request, 'recipies.html', context)

@login_required(login_url="/login/")
def update_receipe(request,id):
    queryset=Recipie.objects.get(id=id)
    

    if request.method == "POST":
        data=request.POST
        r_name=data.get('r_name')
        r_des=data.get('recipies.r_des')
        r_image=request.FILES.get('r_image')  # Matches form field name
        
        queryset.r_name=r_name
        queryset.r_des=r_des

        if 'r_image' in request.FILES:
            data.r_image = request.FILES['r_image']
        
        
        queryset.save()
        return redirect('/recipies/')
    
    context = {'recipies': queryset}
    return render(request, 'update_recipie.html', context)



@login_required(login_url="/login/")
def delete_recipie(request,id):
    queryset=Recipie.objects.get(id=id)
    queryset.delete()
    
    return redirect('/recipies/')


def register(request):

    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)   

        if user.exists():
            messages.error(request, 'Error: Username already taken. Please choose a different username.')
            return redirect('/register/')
          

        user=User.objects.create(
            first_name=first_name,last_name=last_name,
             username= username,
        )

        user.set_password(password)#for encryption
        user.save()
        messages.info(request,'Account created  Successfully !!')
            
        return redirect('/register/')
        
    return render(request,'register.html')



def login_page(request):
     
     if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/login/')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user= authenticate(username=username ,password=password)
        
        if user is None:
            messages.error(request, 'Invalid Password')
            
        
        else:
           login(request, user) #user ko dalna hai session mai
           return redirect('/recipies/')
#to maintain sesson each time value not asked but stored for automatic login
     return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
    