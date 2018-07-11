# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render

# Create your views here.
from .models import Projectname
from .models import Jenkinsjobsname
from .models import Jenkinsjobsinformation
from django.shortcuts import redirect
import datetime


from .forms import PostForm

from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


def index(request):
    project_name=Projectname.objects.order_by('name')
    context = {'categories': project_name}
    return render(request,'buildstatus/job_detail.html', context)


def detail(request,projectname_id):
    project_name=Projectname.objects.order_by('name')

    jobs=Projectname.objects.get(pk=projectname_id)

    context = {'jobs': jobs, 'categories':project_name}
    return render(request,'buildstatus/job_detail.html', context)

def jobdetail(request,projectname_id,jobinformation_id):
    project_name=Projectname.objects.order_by('name')

    jobs=Projectname.objects.get(pk=projectname_id)

    
    jobdetail=Jenkinsjobsname.objects.get(pk=jobinformation_id)
    test=jobdetail.Jenkinsjobsinformation.all()

    page = request.GET.get('page',1)
    paginator=Paginator(test,3)# show 3 results per page

    try: 
       results = paginator.page(page)
    except PageNotAnInteger:
       results = paginator.page(1)
    except EmptyPage:
        results=paginator.page(paginator.num_pages)
               
    context = {'jobs': jobs,'categories':project_name,'results':results}
   
    return render(request,'buildstatus/job_detail.html', context)


def post_edit(request,pk):
    jenkinsjobsinformation = get_object_or_404(Jenkinsjobsinformation,pk=pk)
    print request.method
    if request.method == "POST": 
        form = PostForm(request.POST, instance=jenkinsjobsinformation)
        if form.is_valid():
            jenkinsjobsinformation=form.save(commit=True)
            jenkinsjobsinformation.save()
            return redirect('detail_job')
    else:
        form=PostForm(instance=jenkinsjobsinformation)
    return render(request, 'buildstatus/jenkinsjobsinformation_edit.html', {'form': form})

    

def useradmin(request):
    detail=Jenkinsjobsinformation.objects.all()
    page = request.GET.get('page',1)
    paginator=Paginator(detail,5)# show 3 results per page

    try: 
       results = paginator.page(page)
    except PageNotAnInteger:
       results = paginator.page(1)
    except EmptyPage:
        results=paginator.page(paginator.num_pages)
    context= {'results': results}
    return render(request, 'buildstatus/detail_job.html',context)
    
    
    
    



