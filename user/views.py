from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
import datetime
from django.db import connection
# Create your views here.
def home(request):
    
    cdata=category.objects.all().order_by('-id')[0:6]
    pdata=products.objects.all().order_by('-id')[0:4]
    
    return render(request,'user/index.html',{"data":cdata,"prod":pdata})
    
def about(request):
    return render(request,'user/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        a=request.POST.get("name","")
        b=request.POST.get("mobile","")
        c=request.POST.get("email","")
        d=request.POST.get("msg","")
        x=contact(name=a,email=c,contact=b,message=d)
        x.save()
        status=True
        #return HttpResponse("<script>alert('Thanks for enquiry..');window.location.href='/user/contactus/'</script>")
    return render(request,'user/contactus.html',{'S':status})
    
def services(request):
    return render(request,'user/services.html')

def myorder(request):
    return render(request,'user/myorders.html')

def myprofile(request):
    return render(request,'user/myprofile.html')

def prod(request):
    cdata=category.objects.all().order_by('-id')
    pdata=products.objects.all().order_by('-id')[0:2]
    x=request.GET.get('abc')
    pdata=""
    if x is not None:
        pdata=products.objects.filter(category=x)
    else:
        pdata=products.objects.all().order_by('-id')
        
    return render(request,'user/product.html',{"cat":cdata,"prod":pdata})

def signup(request):
    if request.method=='POST':
        name=request.POST.get("name","")
        mobile=request.POST.get("mobile","")
        email=request.POST.get("email","")
        password=request.POST.get("passwd","")
        address=request.POST.get("address","")
        picname=request.FILES['fu']
        x=profile(name=name,mobile=mobile,email=email,passwd=password,address=address,ppic=picname)
        x.save() 

        return HttpResponse("<script>alert('Your Register succesfully..');window.location.href='/user/signup/' </script>")  
    return render(request,'user/signup.html')

def signup(request):
    status=False
    if request.method=='POST':
        name=request.POST.get("name","")
        Mobile=request.POST.get("mobile","")
        email=request.POST.get("email","")
        Password=request.POST.get("passwd","")
        address=request.POST.get("address","")
        picname=request.FILES['fu']
        d=profile.objects.filter(email=email)

        if d.count()>0:
            return HttpResponse("<script>alert('You are already registered..');window.location.href='/user/signup/'</script>")
        else:
            x=profile(name=name,mobile=mobile,email=email,passwd=password,address=address,ppic=picname)
            x.save() 
        return HttpResponse("<script>alert('You are registered successfully..');window.location.href='/user/signup/'</script>")

        #return HttpResponse("<script>alert('Thanks For SignUp..');window.location.href='/user/signup/';</script>")
    return render(request,'user/signup.html')


def Signin(request):
    if request.method=='POST':

        username=request.POST.get("uname")
        passwd=request.POST.get("passwd")
        checkuser=profile.objects.filter(email=username,passwd=passwd)
        if(checkuser):
            request.session['userid']=username
            return HttpResponse("<script>alert('Logged In Successfully');window.location.href='/user/Signin';</script>")

        else:
            return HttpResponse("<script>alert('UserID or Password is Incorrect');window.location.href='/user/Signin';</script>")
    return render(request,'user/signin.html')


def viewsdetails(request):
    a=request.GET.get('msg')
    data=products.objects.filter(id=a)
    
    return render(request,'user/viewsdetails.html',{"d":data})

def process(request):
    userid=request.session.get('userid')
    pid=request.GET.get('pid')
    btn=request.GET.get('bn')
    print(userid,pid,btn)
    if userid is not None:
       if btn=='cart':
        x=addtocart(pid=pid,userid=userid,status=True,odate= datetime.datetime.now())
        x.save()
       elif btn=='order': 
        order(pid=pid,userid=userid,remarks="pendding",status=True,odate=datetime.datetime.now())
        return HttpResponse("<script>alert('Your order have confirmed...');window.location.href='/user/myorder/'</script>")
        
        return render(request,'user/process.html',{"alreadylogin":True})

    else:
        return HttpResponse("<script>window.location.href='/user/Signin/'</script>")

def logout(request):
    del request.session['userid']
    return HttpResponse("<script>window.location.href='/user/home/'</script>")

def cart(request):
    if request.session.get('userid'):
        userid=request.session.get('userid')
        cursor=connection.cursor()
        cursor.execute("select c.*,p.* from user_addtocart c,user_products p where p.id=c.pid")
        cartdata=cursor.fetchall()
        pid=request.GET.get('pid')
        if request.GET.get('pid'):
            res=addtocart.objects.filter(pid=pid,userid=userid)
            res.delete()
            return HttpResponse("<script>alert('your produt is delete');window.location.href='/user/cart/';</script>")
    return render(request,'user/cart.html',{"cart":cartdata})


  