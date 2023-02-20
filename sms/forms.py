from django import forms
from .models import Student , Class

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = "__all__"
        exclude = ['is_approved',"rf_code"]
        widgets = {
            'dob': DateInput(),
            'contact':forms.TextInput(attrs={'type':'tel'})
        }

class EditStudentForm(forms.ModelForm):
    class Meta():
        model = Student
        exclude = ["is_approved"]
        widgets = {
            'dob': DateInput(),
            'contact':forms.TextInput(attrs={'type':'tel'}),
            'rf_code':forms.TextInput(attrs={'autofocus':True})
        }

class ClassForm(forms.ModelForm):
    class Meta():
        model = Class
        fields = "__all__"
        widgets = {
            'name':forms.Select(attrs={
                'class':'px-4 py-2 border-4 focus:bg-red-400'
            })
        }


