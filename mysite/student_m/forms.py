from django import forms
from .models import student

class StudentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = '__all__'
        labels = {
            "clas" : 'Class',
        }

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['clas'].empty_label = "Select"