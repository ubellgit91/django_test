from django.urls import path
#
from . import views

app_name = 'polls'
urlpatterns = [
    # http://127.0.0.1:8000/polls/1/
    path('', views.IndexView.as_view(), name='index'),
    path('<int:question_id>/', views.DetailView.as_view(), name="detail"), # <int:question_id>/이 부분은 url로 int값이 넘어오면 question_id 라는 이름으로 view에 전송됨.
    path('<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),
]