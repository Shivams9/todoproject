from django.shortcuts import render, HttpResponse
from .forms import TodoForm
from .models import TodoModel
def index(request):
    return HttpResponse("Todo App")
# Create your views here. code here

def all(request):
    data = TodoModel.objects.all().order_by('task').reverse()
    return render(request, 'alltodo.html', {"todo":data})



def form(request):
    if request.POST:
        newdata = TodoForm(request.POST)
        if newdata.is_valid():
            newdata.save(commit=False)
            newdata.save()
            return HttpResponse("data Saved")
    initial = {"task": "todo", "description": "y", "status": "z"}
    #return  HttpResponse("jjhjhhj")
    return render(request, "form.html", {"form": TodoForm()})


