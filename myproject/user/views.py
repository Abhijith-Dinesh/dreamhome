from django.shortcuts import render,redirect
from .models import User
from django.http import JsonResponse

# Create your views here.

def index(request):
    if request.method=='GET':
        users=None
        if 'userid' in request.session:
            users=User.objects.get(pk=request.session['userid'])   
        return render(request,'user/index.html',{'user':users})
def signin(request):
    if request.method=='GET':
        return render(request,'user/signin.html')
    elif request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        users=User.objects.filter(youremail=email,password=password)
        print(users)
        if len(users)==1:
            request.session['userid']=users[0].id
            return redirect(profile)
        else:
            return render(request,'user/signin.html',{'error' : 'invalid email/password'})

def signup(request):
    if request.method=='GET':
        return render(request,'user/signup.html')
    elif request.method=='POST':
        yourname=request.POST['yourname']
        youremail=request.POST['youremail']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            User.objects.create(yourname=yourname,youremail=youremail,phonenumber=phonenumber,password=password)
            return redirect('user_signin')
        else:
            return render(request,'user/signup.html')
        
def logout(request):
    if'userid' in request.session:
        del request.session['userid']
        return redirect('user_index')

# def rent(request):
#     if request.method =='GET':
#          return render(request,'user/rent.html',{'form':RentForm()})
#     else:
#         form = RentForm(request.POST,request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user_id = request.session['userid']
#             obj.save()
#             return redirect(profile)

def plan(request):
    return render(request,'user/plan.html')

def choose(request):
    return render(request,'user/choose.html')

def profile(request):
    if request.method=='GET':
        return render(request,'user/profile.html')

# def rent(request):
#     return render(request,'user/rent.html')
