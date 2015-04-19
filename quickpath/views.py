from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from quickpath.forms import ArticleForm
import findPaths
# Create your views here.

def index(request):
	findPaths.web.clear()
	findPaths.defList = []
	findPaths.visited.clear()
	context = RequestContext(request)
	if request.method == 'POST':
		findPaths.web.clear()
		findPaths.defList = []
		findPaths.visited.clear()
		article_form = ArticleForm(request.POST)
		if article_form.is_valid():
			start_article = article_form.cleaned_data.get('start_article')
			end_article = article_form.cleaned_data.get('end_article')
			try:
				retval = launchSearch(start_article, end_article)
				findPaths.web.clear()
				findPaths.visited.clear()
				findPaths.defList = []
			except:
				retval = 0	
			if (retval == 0):
				return render_to_response('index.html', {'article_form':article_form, 'info':3, 'start':start_article, 'end':end_article}, context)
			if (retval == 3):
				return render_to_response('index.html', {'article_form':article_form, 'info':0, 'start':start_article, 'end':end_article}, context)
			else:	
				print "America"
				return render_to_response('index.html', {'article_form':article_form, 'info':1, 'path':retval, 'start':start_article, 'end':end_article}, context)
		else:
			print article_form.errors
	else:
		article_form = ArticleForm()
		return render_to_response('index.html', {'article_form':article_form, 'info':2}, context)

def launchSearch(start_article, end_article):
	start_article = start_article.replace(' ', '_')
	end_article = end_article.replace(' ', '_')
	retval = findPaths.findPaths(start_article, end_article)
	if (retval == 3):
		print "hie"
	else:
		for i in retval:
			print i
	return retval