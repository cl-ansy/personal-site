from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from attendance.models import CheckIn

@csrf_exempt
def attendance(request):
    if request.method == 'POST':
        key = request.POST.get('Key', '')
#        if CheckIn.objects.filter(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp.date()=datetime.now().date()).distinct():
#            checkin = CheckIn.objects.get(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp=datetime.now())
        if key  == 'PuN5XfYtn':
            checkin = CheckIn()
            checkin.studentID = request.POST.get('StudentID', '')
            checkin.classID = request.POST.get('ClassID', '')
            checkin.timestamp = datetime.now()
            checkin.save()
    checkins = CheckIn.objects.order_by("-timestamp")
    return render_to_response('attendance.html', {'checkins':checkins}, context_instance=RequestContext(request))
