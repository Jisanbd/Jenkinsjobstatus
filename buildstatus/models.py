# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Projectname(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Jenkinsjobsname(models.Model):
    projectname=models.ForeignKey(Projectname)
    jobsname = models.CharField(max_length=200)
    def __str__(self):
        return self.jobsname

    def get_absolute_url(self):
        return reverse('job_detail',kwargs={'projectname_id': self.projectname.pk, 'jobinformation_id': self.pk})
 

class Jenkinsjobsinformation(models.Model):
    jobinformation=models.ForeignKey(Jenkinsjobsname,on_delete=models.CASCADE,related_name="Jenkinsjobsinformation")
    build = models.IntegerField()
    date = models.DateField(null=True)
    #tag = models.ImageField(upload_to='static/jlr/img/', blank=True)
    Status_choices=(
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
    )
    Smoke_choices=(
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
    )
    Sanity_choices=(
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
    )
    System_choices=(
        ('SUCCESS', 'SUCCESS'),
        ('FAILURE', 'FAILURE'),
    )
    Releasecandidate_choices=(
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    
    Status=models.CharField(max_length=10,choices=Status_choices,default='SUCCESS')
    Smoke=models.CharField(max_length=10,choices=Smoke_choices,default='SUCCESS')
    Sanity=models.CharField(max_length=100,choices=Sanity_choices,default='SUCCESS')
    System=models.CharField(max_length=100,choices=System_choices,default='SUCCESS')
    Releasecandidate=models.CharField(max_length=100,choices=Releasecandidate_choices,default='YES')
    JIRA_open=models.CharField(max_length=100,null=True)
    JIRA_closed=models.CharField(max_length=100,null=True)


