from django import forms

from .models import Jenkinsjobsinformation

class PostForm(forms.ModelForm):

    class Meta:
        model = Jenkinsjobsinformation
        fields = ('build', 'date','Status','Sanity','Smoke','System','Releasecandidate','JIRA_open','JIRA_closed')
