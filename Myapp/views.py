from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *


def demo(request):
    return HttpResponse("dfdghjhkjljb")
    
def nfunc(request):
    return HttpResponse('hello there')

def demo1(request):
    data={'name':'adhithya'}
    return render(request,'page1.html',{'datas':data})
def func(request):
    data1={'greet':'hello there'}
    return render(request,'page2.html',{'ndata':data1})

def fun1(request):
    data1=[{'name':'hello there'},
          {'name':'adhithya'},
          {'name':'hello there'},
          {'name':'adhithya'}]
    return render(request,'page1.html',{'ndata':data1})
def fun2(request):
    data1=[{'name':'hello there'},
          {'name':'Adhithiy'},
          {'name':'over here'},
          {'name':'welcome to my page'}]
    return render(request,'page2.html',{'ndata':data1})


#######################################################################################

# def reads(request):
#     user=User.objects.all()
#     return render(request,'view.html',{'data':user})

# def create(request):
#     if request.method=='POST':
#        name1=request.POST['names'] 
#        age1=request.POST['ages']   
#        place1=request.POST['places'] 
#        User.objects.create(name=name1,age=age1,place=place1)
#        return redirect('read')
#     return render(request,'create.html')

# def delete(request,id):
#     user=User.objects.get(id=id)
#     user.delete()
#     return redirect('read')
    
# def update(request,id):
#     user=User.objects.get(id=id)
#     if request.method=='POST':
#        name1=request.POST['names'] 
#        age1=request.POST['ages']   
#        place1=request.POST['places']
#        user.name=name1
#        user.age=age1
#        user.place=place1
#        user.save()
#        return redirect('read')
#     return render(request,'update.html',{'data':user})

       
       
    

#######################################################################################
# def emreads(request):
#     userem=Employee.objects.all()
#     return render(request,'emview.html',{'emdata':userem})

from django.db.models import Q

def search_and_read(request):
    if request.method == 'POST':
        search_query = request.POST.get('searchs', ' ').strip()
        if search_query:
            data = Employee.objects.filter(
                Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
            )
        else:
            data = Employee.objects.all()
    else:
        data = Employee.objects.all()
        
    return render(request,"emview.html",{'data':data})
    
    


def emcreate(request):
    if request.method=='POST':
       name1=request.POST['first_name'] 
       lname1=request.POST['last_name']   
       email1=request.POST['email'] 
       department1=request.POST['department'] 
       salary1=request.POST['salary']   
       Employee.objects.create(first_name=name1,last_name=lname1,email=email1,department=department1,salary=salary1)
       return redirect('reads')
    return render(request,'emcreate.html')

def emdelete(request,id):
    user=Employee.objects.get(id=id)
    user.delete()
    return redirect('reads')
    
def emupdate(request,id):
    user=Employee.objects.get(id=id)
    if request.method=='POST':
       name1=request.POST['first_name'] 
       lname1=request.POST['last_name']   
       email1=request.POST['email'] 
       department1=request.POST['department'] 
       salary1=request.POST['salary']   
       user.first_name=name1
       user.last_name=lname1
       user.email=email1
       user.department=department1
       user.salary=salary1
       user.save()
       return redirect('reads')
    return render(request,'update.html',{'emdata':user})
#######################################################################################


def search_and_read(request):
    if request.method == 'POST':
        search_query = request.POST.get('searchs', ' ').strip()
        if search_query:
            data = product.objects.filter(
                Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
            )
        else:
            data = product.objects.all()
    else:
        data = product.objects.all()
        
    return render(request,"prview.html",{'prdata':data})
    
 
 
    


def prcreate(request):
    if request.method=='POST':
       name1=request.POST['name'] 
       category1=request.POST['category']   
       price1=request.POST['price'] 
       stock_quantity1=request.POST['stock_quantity'] 
       description1=request.POST['description']   
       product.objects.create(name=name1,category=category1,price=price1,stock_quantity=stock_quantity1,description=description1)
       return redirect('reads')
    return render(request,'prcreate.html')

def prdelete(request,id):
    user=product.objects.get(id=id)
    user.delete()
    return redirect('reads')
    
def prupdate(request,id):
    user=product.objects.get(id=id)
    if request.method=='POST':
       name1=request.POST['name'] 
       category1=request.POST['category']   
       price1=request.POST['price'] 
       stock_quantity1=request.POST['stock_quantity'] 
       description1=request.POST['description']  
       user.name=name1
       user.category=category1
       user.price=price1
       user.stock_quantity=stock_quantity1
       user.description=description1
       user.save()
       return redirect('reads')
    return render(request,'prupdate.html',{'prdata':user})

                
       
               
       
         
    