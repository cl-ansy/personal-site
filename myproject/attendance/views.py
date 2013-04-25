from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from attendance.models import CheckIn

@csrf_exempt
def attendance(request):
#    if request.method == 'POST':
#        #if CheckIn.objects.filter(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp.date()=datetime.now().date()).distinct():
#         #   checkin = CheckIn.objects.get(studentID=request.POST['StudentID'],classID=request.POST['ClassID'],timestamp=datetime.now())
#        #else:
#        s_id = request.POST.get('StudentID', '')
#        c_id = request.POST.get('ClassID', '')
#        checkin = CheckIn()
#        checkin.studentID = 1324        
#        checkin.studentID = s_id
#        checkin.classID = c_id
#        checkin.timestamp = datetime.now()
#        checkin.save()
#    else:
    checkin = CheckIn.objects.all()
    return render_to_response('attendance.html', {'checkin':checkin}, context_instance=RequestContext(request))
