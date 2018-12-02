from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View, DetailView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from .models import Question, Choice
# Create your views here.


class IndexView(View):

    def get(self, request):
        # __lte는 gt lt 할때 그거임 작거나 같다. 니까 <= 기호라고 보면 됨. filter는 where조건이라고 보면 된다.
        latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # output = ', '.join([q.question_text for q in latest_question_list])
        context = { 'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html' # template_name을 오버라이딩 하지 않으면 <app>/<model>_list.html 로 자동맵핑됨.
#     context_object_name = 'latest_question_list' # ListView의 경우, 자동 생성되는 컨텍스트<템플릿으로 넘겨질 값>가 담긴 컨텍스트 변수의 이름은 question_list이다.
#                                                   # 하지만 context_object_name 속성을 오버라이딩해서, 값을 지정해주면 그 값이 컨텍스트의 이름이 된다.
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]   # get_querset() 메소드의 리턴값을 통해 ListView가 어떤 모델을 쓰는지 알아내는 거 같다.


class DetailView(View):
    # 뭐지? 쿼리스트링(get) ? ~~방식으로 안넘기고 걍 url패턴대로 /로 구분하여 값을 넘겼는데도 get으로 받네?
    def get(self, request, question_id):
        # try:
        #     question = Question.objects.get(pk=question_id)
        # except Question.DoesNotExist:
        #     raise Http404("Question does not exist")
        question = get_object_or_404(Question, pk=question_id) # 위에 코드를 한줄로 축약시켜줌. 그래서 shotcut 라이브러리에 있음..
        return render(request, 'polls/detail.html', {'question': question})

# generic 뷰로 구성해보기.
class ResultsView(DetailView):
    model = Question # 해당 뷰에서 사용할 model을 지정함.
    # 기본적으로 DetailView 제너릭 뷰는 <app name>/<model name>_detail.html 템플릿을 사용 _detail! 이렇게 생긴 템플릿으로 자동으로 찾아간다는 뜻임.
    template_name = 'polls/results.html' # 이렇게 템플릿네임 변수를 오버라이딩해서 지정해주면 해당 템플릿으로 찾아간다.
    # template_name을 오버라이딩하지 않으면 <app>/<model>_detail.html 이라는 템플릿으로 자동으로 맵핑됨.
    # DetailView의 경우, context로 쓰이는 변수가 model명과 일치하게 자동으로 제공된다. 즉 question이라는 변수!에 디테일템플릿으로 넘길 모델이 자동으로 담겨있다.



class VoteView(View):

    def get(self, request, question_id):
        return HttpResponse("Voting on questions %s" % question_id)

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice']) # question모델과 엮인 Choice의 모델의 객체를 하나 get해옴.
        except (KeyError, Choice.DoesNotExist):
            context = {'question': question, 'error_message': "You don't select a Choice"}
            return render(request, 'polls/detail.html', context)
        else:
            # c.wheel_set.all() # returns all Wheel objects related to c 라는 구문을 보자.
            #
            # question.choice_set.get(pk=request.POST['choice'])
            # 즉 question 모델과 관련된 choice 모델객체를 반환받는다. get이니까 pk값이 Post로 받은 choice의 값과 일치하는
            # question과 엮인 choice모델 객체를 반환받는다는 소리이다..
            selected_choice.votes += 1 # Choice의 모델?의 객체가 담겨있는데, 그 인스턴스의 변수 votes에 += 1을 더해줌.
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # reverse()는 네임스페이스로 url을 이용가능하게 해줌.
