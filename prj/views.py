from django.shortcuts import render, get_object_or_404
from .models import Prject

def prj_list(request):
    projects = Prject.objects.order_by('name_prj')
    return render(request, 'prj/prj_list.html', {'projects': projects})

def prj_detail(request, pk):
    projectdetails = get_object_or_404(Prject, pk=pk)
    return render(request, 'prj/prj_detail.html', {'projectdetails': projectdetails})
