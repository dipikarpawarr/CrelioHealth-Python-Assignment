from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.

class Class_Model(models.Model):
    ID = models.IntegerField(primary_key=True)
    Class = models.CharField(max_length=1)

    class Meta:
        db_table = 'Class'

    def __str__(self):
        return self.Class

class Stud_Registration_Model(models.Model):
    FirstName = models.CharField(max_length=100)
    MiddletName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'), ('Unisex', 'Unisex/Parody'))
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Pincode = models.CharField(max_length=6)
    MobileNumber = models.CharField(max_length=10)
    ParentName = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=50)
    Class = models.ForeignKey(Class_Model, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'Registration'

    def __str__(self):
        return self.FirstName +" "+ self.MiddletName +" "+ self.LastName

class Add_Assignment_Model(models.Model):
    Class = models.ForeignKey(Class_Model, on_delete=models.CASCADE, null=False)
    AssignmentName = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField()
    AddedBy = models.CharField(max_length=100, null=False)
    AddedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Assignment'

    def __str__(self):
        return self.AssignmentName

class Assignment_Marks_Model(models.Model):
    ID = models.IntegerField(primary_key=True)
    Marks = models.CharField(max_length=6)

    class Meta:
        db_table = 'Assignment_Marks'

    def __str__(self):
        return self.Marks

class Fill_Assignment_Report_Model(models.Model):
    Class = models.ForeignKey(Class_Model, on_delete=models.CASCADE, null=False)
    Assignment = models.ForeignKey(Add_Assignment_Model, on_delete=models.CASCADE, null=False)
    Student = models.ForeignKey(Stud_Registration_Model, on_delete=models.CASCADE, null=False)
    Marks = models.ForeignKey(Assignment_Marks_Model, on_delete=models.CASCADE, null=False)
    AddedBy = models.CharField(max_length=100, null=False, default="user")
    AddedDate = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Fill_Assignment_Report'

class Login_Model(models.Model):
    Username = models.CharField(max_length=40)
    Password = models.CharField(max_length=40)
    class Meta:
        db_table = 'Login'

class Class_Student_Data_For_Dashboard_Model(models.Model):
    ClassName = models.CharField(max_length=100)
    TotalStudents = models.IntegerField(null=True)

    class Meta:
        db_table = 'Class_Student_Data'
