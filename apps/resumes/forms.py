from django import forms

class ResumeFilterForm(forms.Form):
    SKILLS_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('SQL', 'SQL'),
        ('JavaScript', 'JavaScript'),
    ]

    skills = forms.MultipleChoiceField(
        choices=SKILLS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '标签,逗号分隔'}))
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='上传时间起'
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='上传时间止'
    )
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '技能关键词'}),
        label='技能搜索'
    )

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        return [tag.strip() for tag in tags.split(',') if tag.strip()]