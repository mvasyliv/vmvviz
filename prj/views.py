from django.shortcuts import render
from .models import Prject

def prj_list(request):
    projects = Prject.objects.all()
    return render(request, 'prj/prj_list.html', {'projects' : projects})