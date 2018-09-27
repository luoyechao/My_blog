from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import Http404
from markdown import markdown
from django.shortcuts import redirect
# Create your views here.

def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':post_list})
#    return self.write("hello world")


def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
        post.content = markdown(post.content,extensions=[
                                                 'markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc',
                                                 ])
        #post.content = markdown(post.content,['codehilite'])
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,'error':False})

def about_me(request):
    return render(request,'aboutme.html')

def search_tag(request,tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})
def blog_search(request):
    if 's' in request.GET:
        s=request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list)==0:
                return render(request,'archives.html',{'post_list':post_list,'error':True})
            else:
                return render(request,'archives.html',{'post_list':post_list,'error':False})

    return redirect('/')
