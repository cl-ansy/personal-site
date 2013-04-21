from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def attendance(request):
    #html = "<html><body>Coming Soon...</body></html>"
    #return HttpResponse(html)
    if request.method == 'POST':
        form = CheckInForm(request)
        if form.isValid():
            form.save()
        else:
            form = CheckInForm()
    else:
        form = CheckInForm()
    return render_to_response('attendance.html', {'form': form}, context_instance=RequestContext(request))
