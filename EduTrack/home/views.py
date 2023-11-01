from django.shortcuts import render
from django.template.context_processors import csrf
# from .models import Users
from django.contrib import messages

def home(request):
    return render(request,"home/home.html",{})

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'home/login.html',c)

def validate(request):
    if(request.method=='POST'):
        username = request.POST.get('username','')
        password = request.POST.get('pass','')
        if(username is not None and password is not None):
            # flag1 = False
            # flag2 = False
            try:
                u = Users.objects.get(username = username)
            except:
                messages.error(request,"Invalid Username")
                return render(request,'home/login.html') 

            if(u.password == password):
                request.session['username'] = username
                # request.session['password'] = password
                uname={
                    "username":username
                }      
                return render(request,'home/visualize.html', uname)
            else:
                messages.error(request,"Invalid Password")
                return render(request,'home/login.html')    
        else:
            messages.success(request,'Credentials cannot be empty')
            return render(request,'home/login.html')
    
    elif(request.method == "GET"):
        if(request.session.get('username',False)):
            username = request.session.get('username',False)
            uname={
                    "username":username
            }     
            return render(request,'home/verified.html', uname)    
    
    else:
        return render(request,'home/login.html')