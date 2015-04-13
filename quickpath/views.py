from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = RequestContext(request)
	return render_to_response('index.html', context)
