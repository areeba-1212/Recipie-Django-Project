from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

def home(request):
#list has dictionary
    peoples=[{'name': 'ali khan ','age': 26},
             {'name': 'sara khan ','age': 2},
              {'name': 'afan sajid ','age': 400}]
    
    return render(request,"index.html",context={'peoples':peoples})

def about(request):
       return render(request,"about.html")
def contact(request):
       return render(request,"contact.html")