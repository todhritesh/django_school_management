from django import forms
from .models import Student

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = "__all__"
        exclude = ['is_approved']
        widgets = {
            'dob': DateInput(),
            'contact':forms.TextInput(attrs={'type':'tel'})
        }


