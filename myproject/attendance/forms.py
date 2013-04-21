import django.forms 
from attendance import models

class CheckInForm(forms.ModelForm):

    class meta:
        model = models.CheckIn

