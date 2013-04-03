from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponse

def home(request):
    #html = "<html><body>Coming Soon...</body></html>"
    #return HttpResponse(html)
    return render_to_response('home.html', {"foo": "bar"}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {"foo": "bar"}, context_instance=RequestContext(request))

def resume(request):
    return render_to_response('resume.html', {"foo": "bar"}, context_instance=RequestContext(request))

def training(request):
    return render_to_response('training.html', {"foo": "bar"}, context_instance=RequestContext(request))
