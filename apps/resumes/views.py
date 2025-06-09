from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Resume
from .forms import ResumeUploadForm

class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    template_name = 'resumes/list.html'
    paginate_by = 10

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class ResumeUploadView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeUploadForm
    success_url = '/resumes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.file_type = self.request.FILES['file'].name.split('.')[-1]
        return super().form_valid(form)

def resume_search(request):
    # 实现基于关键词/标签/技能的搜索功能
    query = request.GET.get('q')
    results = Resume.objects.filter(
        Q(tags__icontains=query) |
        Q(skills__icontains=query) |
        Q(file_name__icontains=query)
    ).filter(user=request.user)
    return render(request, 'resumes/search.html', {'results': results})