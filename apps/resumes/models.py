from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/%Y/%m/%d/')
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True)
    skills = models.TextField(blank=True)


    def __str__(self):
        return f"{self.user_id.username}'s Resume"
