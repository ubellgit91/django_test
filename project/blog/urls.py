from django.urls import path, re_path
from . import views

app_name = 'blog' # 네임스페이스를 지정함.
# the 'name' value as called by the {% url %} template tag
# 정규식이 있는 path는 re_path()를 이용.
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about', views.About.as_view(), name='about'),
    # path('/diary', views.Diary.as_view(), name='diary'),
]