from attendance.models import CheckIn
from django.contrib import admin

class CheckInAdmin(admin.ModelAdmin):
    fields    = ['studentID', 'classID', 'timestamp']

admin.site.register(CheckIn,CheckInAdmin)
