from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
# Create your views here.
def attendance(request):
    #html = "<html><body>Coming Soon...</body></html>"
    #return HttpResponse(html)
    now = datetime.now()
    today=now.day
    month=now.month
    s_id = request.POST['StudentID']
    c_id = request.POST['ClassID']
    if request.method == 'POST':
        if CheckIn.objects.filter(studentID=s_id,classID=c_id,timestamp__date=now.date) not Null:
            checkin = CheckIn.objects.get(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp=now)
        else:
           
            checkin = CheckIn()
            checkin.studentID=s_id
            checkin.classID=c_id
            checkin.timestamp = now
            checkin.save()
    return render_to_response('attendance.html', {'checkin',checkin}, context_instance=RequestContext(request))
