from django.shortcuts import render, redirect

# Post 모델을 import
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post() # post를 인스턴스화
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/post/{post.id}/')



def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')


def edif(request, id):
    post = Post.objects.get(id=id)

    return render(request, 'edit.html', context) # 직접 html을 보여줄때 활용

def update(request, id):
    #기존 데이터
    post = Post.objects.get(id=id)

    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = post() 새로운 개시물을 만들때 사용
    # 기존의 게시물을 가져올때
    post.title = title 
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}')