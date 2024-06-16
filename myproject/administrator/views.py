from django.shortcuts import render,redirect
from .forms import RentForm,Rent
# Create your views here.


def rent(request):
    if request.method =='GET':
         return render(request,'administrator/rent.html',{'form':RentForm()})
    else:
        form = RentForm(request.POST,request.FILES)
        if form.is_valid():
            # obj = form.save(commit=False)
            # obj.user_id = request.session['userid']
            # obj.save()
            form.save()
            return redirect('admin_rent')

def managerent(request):
    if request.method =='GET':
     return render(request,'administrator/manage.html',{'data':Rent.objects.all()})

def editrent(request,id):
    rent = Rent.objects.get(pk=id)
    if request.method =='GET':
        context ={
             'form':RentForm(instance=rent)
        }
        return render(request,'administrator/edit.html',context)
    else:
        form = RentForm(data=request.POST,files=request.FILES,instance=rent)
        if form.is_valid():
            form.save()
            return redirect('admin_rent')
        else:
            return redirect('admin_manage')

def deleterent(request,id):
    Rent.objects.get(pk=id).delete()
    return redirect('admin_manage')