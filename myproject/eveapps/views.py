from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponse

def eveapp_index(request):
    return render_to_response('eveapp_index.html', {}, context_instance=RequestContext(request))

def testappone(request):
    return render_to_response('testappone.html', {"foo": "bar"}, context_instance=RequestContext(request))

def testapptwo(request):
    return render_to_response('testapptwo.html', {"foo": "bar"}, context_instance=RequestContext(request))
