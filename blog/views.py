from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse, Http404
from .models import Article, Category

def home(request):
	context = {
		'articles': Article.objects.published(),
	}

	return render(request, 'blog/home.html', context)

def detail(request, slug):
	context ={
		'article': get_object_or_404(Article.objects.published(), slug=slug),
		'category': Category.objects.filter(status=True)
	}
	
	return render(request, 'blog/detail.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug, status=True)
	context ={
		'category': category,
	}
	
	return render(request, 'blog/category.html', context)