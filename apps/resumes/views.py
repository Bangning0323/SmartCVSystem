# views.py 高级查询视图
from django.views.generic import ListView
from django.db.models import Q
from .models import Resume
from .forms import ResumeFilterForm


class ResumeSearchView(ListView):
    model = Resume
    template_name = 'resumes/list.html'
    paginate_by = 10
    context_object_name = 'resumes'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ResumeFilterForm(self.request.GET)

        if form.is_valid():
            skills = form.cleaned_data['skills']
            tags = form.cleaned_data['tags']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            keyword = form.cleaned_data['keyword']

            # 技能多选过滤
            if skills:
                query = Q()
                for skill in skills:
                    query |= Q(skills__icontains=skill)
                queryset = queryset.filter(query)

            # JSON字段标签过滤
            if tags:
                queryset = queryset.filter(tags__contains=tags)

            # 日期范围过滤
            if start_date and end_date:
                queryset = queryset.filter(
                    upload_date__date__range=(start_date, end_date)
                )
            elif start_date:
                queryset = queryset.filter(
                    upload_date__date__gte=start_date
                )
            elif end_date:
                queryset = queryset.filter(
                    upload_date__date__lte=end_date
                )

            # 关键词全文搜索
            if keyword:
                queryset = queryset.filter(
                    Q(skills__icontains=keyword) |
                    Q(tags__icontains=keyword)
                )

        return queryset.select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ResumeFilterForm(self.request.GET)
        return context