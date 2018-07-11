# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Projectname
from .models import Jenkinsjobsname
from .models import Jenkinsjobsinformation


"""
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'buildname', 'environment', 'tcid','result','date','test_suite','notes','tsname_id')
    list_filter=('date','test_suite','result')
    ordering = ('-tsname_id',)
    pass
"""

class ProjectnameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    pass

class JenkinsjobsnameAdmin(admin.ModelAdmin):
    list_display = ('id','projectname','jobsname')
    pass

class JenkinsjobsinformationAdmin(admin.ModelAdmin):
    list_display = ('id','jobinformation','build','date')

admin.site.register(Projectname,ProjectnameAdmin)
admin.site.register(Jenkinsjobsname,JenkinsjobsnameAdmin)
admin.site.register(Jenkinsjobsinformation,JenkinsjobsinformationAdmin)


