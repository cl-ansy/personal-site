from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
# Create your views here.
def attendance(request):
    #html = "<html><body>Coming Soon...</body></html>"
    #return HttpResponse(html)
    if request.method == 'POST':
        if CheckIn.objects.filter(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp.date()=datetime.now().date()).distinct():
            checkin = CheckIn.objects.get(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp=datetime.now())
        else:
            s_id = request.POST['StudentID']
            c_id = request.POST['ClassID']
            checkin = CheckIn()
            checkin.studentID=s_id
            checkin.classID=c_id
            checkin.timestamp = datetime.now()
            checkin.save()
    return render_to_response('attendance.html', {'checkin',checkin}, context_instance=RequestContext(request))
