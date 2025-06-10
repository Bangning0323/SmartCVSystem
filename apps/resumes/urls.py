from django.urls import path

from apps.resumes.views import ResumeSearchView

app_name = "resume"

urlpatterns = [
    path('resumes/', ResumeSearchView.as_view(), name='resume-search'),
]
