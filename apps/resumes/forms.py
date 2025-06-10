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
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'label,label,....'}))
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Start date'
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='End Date'
    )
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Skill keyword'}),
        label='Skill keyword search'
    )

    def clean_tags(self):
        tags = self.cleaned_data.get('tags', '')
        return [tag.strip() for tag in tags.split(',') if tag.strip()]