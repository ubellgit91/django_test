from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
#
from .models import Post
from .forms import PostForm
# Create your views here.

# 클래스 뷰


class Index(View):
    def get(self, request): # get 방식으로 접근.
        return render(request, 'blog/index.html')


class About(View):
    def get(self, request):
        return render(request, 'blog/about.html')


class Post(View):

    def get(self, request):
        pass
    def post(self, request):
        return redirect('post_detail',)


class PostList(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, '', {'post': post})

    def post(self, request):
        form = PostForm(request.POST)

def post_new(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PostForm(request.POST) #POST 정보를 인자값으로 넘겨 POST정보를 담은 PostForm 객체를 만든다. 클래스명()은 객체생성임. 즉 폼 객체 생성.
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PostForm()
        return render(request, 'name.html', {'form': form})


