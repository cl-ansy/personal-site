from django.db import models

# Create your models here.
class CheckIn(models.Model):
  #Model Fields
  studentID = models.CharField(max_length=10)
  classID = models.CharField(max_length=10)
  timestamp = models.DateTimeField()
  
  def __unicode__(self):
    return self.studentID 
  
