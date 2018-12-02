from django.forms import ModelForm
from .models import Post

# ModelForm 은 Model에 있는 모델클래스를 기반으로 그 모델에 들어갈 데이터의 양식에 맞는 form을 생성해준다.
# 생성자의 인자값으로 request값을 넘겨받으면 넘겨받은 request 값과 모델에 있는 필드의 값을 맵핑시켜줌.
# request는 name 속성의 값과 필드의 값이 일치해야함.


class PostForm(ModelForm):
    class Meta:
        model = Post # 어떤 Model에 대한 form인지 지정한다.
        fields = ['title', 'text', 'author'] # Model에서 어떤 field에 대한 form을 갖을건지 지정한다.