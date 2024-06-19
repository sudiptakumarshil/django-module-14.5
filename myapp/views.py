from django.shortcuts import render
from .forms import MyPracticeForm

# Create your views here.
def create_project(request):
	form = MyPracticeForm()
	return render(request, "create_project.html", {'form':form})
