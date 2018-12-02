# django_core
from django.db import models
from django.utils import timezone
#
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # ForeignKey(외래키)를 auth.User로 설정함. auth.User에 등록된 사람만 해당 칼럼에 들어갈 수 있음.
    title = models.CharField(max_length=300, blank=True, null=False)
    text = models.TextField(blank=True, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    delete_yn = models.CharField(max_length=3, null=False, blank=False, default='n')

    def __str__(self):
        return self.title

    def delete_post(self):
        self.delete_yn = 'y'
        self.save()


class Comment(models.Model):
    author = models.CharField(max_length=10, blank=False, null=False)
    pwd = models.CharField(max_length=20, blank=False, null=False)
    comment = models.TextField(blank=True, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    delete_yn = models.CharField(max_length=3, null=False, blank=False, default='n')

    def __str__(self):
        return self.comment

    def delete_comm(self):
        self.delete_yn = 'y'
        self.save()

