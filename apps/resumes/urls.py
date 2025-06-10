from django.urls import path

from apps.resumes.views import  ResumeListView

app_name = "resume"

urlpatterns = [
    path('list/', ResumeListView.as_view(), name='resume-search'),
]
