from django import forms
from .models import *

def isMobileNumber(number):
    if len(number) != 10 and number.isdigit():
        raise forms.ValidationError("Mobile number must be 10 digit")
    return number

class Registration_Form(forms.ModelForm):
    MobileNumber = forms.CharField(max_length=10, validators=[isMobileNumber])
    class Meta:
        model = Stud_Registration_Model
        fields = '__all__'

class Update_Student_Form(forms.ModelForm):
    class Meta:
        model = Stud_Registration_Model
        fields = '__all__'

class Add_Assignment_Form(forms.ModelForm):
    StartDate = forms.DateField(input_formats=['%d/%m/%Y',])
    EndDate = forms.DateField(input_formats=['%d/%m/%Y',])
    AddedBy = forms.CharField(max_length=100, initial='user', widget=forms.HiddenInput())

    class Meta:
        model = Add_Assignment_Model
        fields = '__all__'
        widgets = {'AddedDate': forms.HiddenInput()}

class Update_Assignment_Form(forms.ModelForm):
    AddedBy = forms.CharField(max_length=100, initial='user', widget=forms.HiddenInput())
    class Meta:
        model = Add_Assignment_Model
        fields = '__all__'

class Delete_Assignment_Form(forms.ModelForm):
    AddedBy = forms.CharField(max_length=100, initial='user', widget=forms.HiddenInput())
    class Meta:
        model = Add_Assignment_Model
        fields = '__all__'

class Delete_Student_Form(forms.ModelForm):
    class Meta:
        model = Stud_Registration_Model
        fields = '__all__'

class Login_Form(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login_Model
        fields = '__all__'

class Fill_Assignment_Report_Form(forms.ModelForm):
    class Meta:
        model = Fill_Assignment_Report_Model
        fields = '__all__'
        widgets = {'AddedBy': forms.HiddenInput(), 'AddedDate': forms.HiddenInput()}