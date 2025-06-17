from django.shortcuts import render,redirect,get_object_or_404
from .models import task
from .forms import taskform

# Create your views here.

def index(request):
    obj = task.objects.all().order_by('date','time')
    return render(request , 'index.html' ,{'task':obj})

def create(request):
    if request.method == 'POST':
        form =taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = taskform()
    return render(request, 'create.html',{'form':form})

def update(request, id):
    obj =get_object_or_404(task, id=id)
    if request.method == 'POST':
        form = taskform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = taskform(instance=obj)
    return render(request, 'create.html',{'form':form})

def delete(request, id):
     obj =get_object_or_404(task, id=id)
     obj.delete()
     return redirect('index')

