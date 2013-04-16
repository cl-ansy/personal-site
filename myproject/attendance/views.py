from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def attendance(request):
    #html = "<html><body>Coming Soon...</body></html>"
    #return HttpResponse(html)
    return render_to_response('attendance.html', {"foo": "bar"}, context_instance=RequestContext(request))
