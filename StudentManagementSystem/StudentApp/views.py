from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def Registraion_View(request):
    form = Registration_Form()
    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
                Class_Student_Data_For_Dashboard()
            return AllStudents_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request,'Registration.html',{'form':form})


def AllStudents_View(request):
    records = Stud_Registration_Model.objects.all()
    return render(request, 'AllStudents.html', {'allStudents': records})

def All_Assignments_View(request):
    records = Add_Assignment_Model.objects.all()
    Classes = Class_Model.objects.all()
    return render(request, 'All_Assignments.html', {'allAssignments': records,'classes':Classes})

def Home_View(request):
    return render(request,'Home.html')

def Update_Student_View(request,id):
    item = Stud_Registration_Model.objects.get(id=id)
    form = Update_Student_Form(instance=item)
    if request.method == 'POST':
        form = Update_Student_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                item = Stud_Registration_Model.objects.get(id=id)
                form = Update_Student_Form(request.POST, instance=item)
                form.save()
                return AllStudents_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request, 'UpdateStudent.html', {'form': form})

def Update_Assignment_View(request,id):
    item = Add_Assignment_Model.objects.get(id=id)
    form = Update_Assignment_Form(instance=item)
    if request.method == 'POST':
        form = Update_Assignment_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                data = form.cleaned_data
                data['AddedBy'] = GetLoggedInUser(request)
                item = Add_Assignment_Model.objects.get(id=id)
                form = Update_Assignment_Form(request.POST, data, instance=item)
                form.save()
                return All_Assignments_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request,'UpdateAssignment.html',{'form':form})

def Delete_Assignment_View(request,id):
    record = Add_Assignment_Model.objects.get(id=id)
    form = Delete_Assignment_Form(instance=record)
    if request.method == 'POST':
        form = Delete_Assignment_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                record = Add_Assignment_Model.objects.get(id=id)
                record.delete()
                return All_Assignments_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request,'DeleteAssignment.html', {'form':form})

def Delete_Student_View(request,id):
    record = Stud_Registration_Model.objects.get(id=id)
    form = Delete_Student_Form(instance=record)
    if request.method == 'POST':
        form = Delete_Student_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                record = Stud_Registration_Model.objects.get(id=id)
                record.delete()
                return AllStudents_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request,'DeleteStudent.html', {'form':form})

def Add_Assignment_View(request):
    form = Add_Assignment_Form()
    if request.method == 'POST':
        form = Add_Assignment_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                data = form.cleaned_data
                data['AddedBy'] = GetLoggedInUser(request)
                form = Add_Assignment_Form(data)
                form.is_valid()
                form.save()
            return Home_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request, 'Add_Assignment.html', {'form': form})


def Fill_Assignment_Report_View(request):
    form = Fill_Assignment_Report_Form()
    if request.method == 'POST':
        form = Fill_Assignment_Report_Form(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                data = form.cleaned_data
                data['AddedBy'] = GetLoggedInUser(request)
                form = Fill_Assignment_Report_Form(data)
                form.is_valid()
                form.save()
            return Home_View(request)
        else:
            return HttpResponse("<h2><i>You are not authenticated User</i></h2>")
    return render(request, 'Fill_Assignment_Report.html', {'form': form})

def GetLoggedInUser(request):
    currentUser = request.user
    return currentUser

def Dashboard_view(request):
    return render(request, 'Dashboard.html',{})

def Dashboard_Data(request):
    dataset = Class_Student_Data_For_Dashboard_Model.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def Class_Student_Data_For_Dashboard():
    createTab = Class_Student_Data_For_Dashboard_Model.objects.create()
    classAndStudentInfo = Class_Student_Data_For_Dashboard_Model.objects.all()

    classes = Class_Model.objects.all()
    students = Stud_Registration_Model.objects.all()
    if bool(classes):
        if classAndStudentInfo.count == 0:
            for classRecord in classes:
                count=0
                for student in students:
                    if classRecord.ID == student.Class_id:
                        count += 1
                insertRecord = Class_Student_Data_For_Dashboard_Model(ClassName=classRecord.Class, TotalStudents=count)
                insertRecord.save()
        else:
            # last Registered student
            lastInsertedStudent = Stud_Registration_Model.objects.last()

            for classRecord in classes:
                if classRecord.ID == lastInsertedStudent.Class_id:
                    updateRecord = Class_Student_Data_For_Dashboard_Model.objects.get(ClassName=classRecord.Class)
                    updateRecord.TotalStudents = updateRecord.TotalStudents + 1
                    updateRecord.save()
    else:
        return HttpResponse("<h2>Please Register the student in the class</h2>")

def Student_Details_View(request):
    classes = Class_Model.objects.all()
    if request.method == 'POST':
        studentsData = Stud_Registration_Model.objects.all()
    return render(request,'Student_Wise_Report.html',{'classes':classes})

def Student_Report_View(request,id):
    studentData = Stud_Registration_Model.objects.filter(Class_id=id)
    classes = Class_Model.objects.get(ID=id)
    assignments = Add_Assignment_Model.objects.filter(Class_id=id)
    marks = Fill_Assignment_Report_Model.objects.filter(Class_id=id)
    marksDetails = Assignment_Marks_Model.objects.all()
    return render(request,'Student_Report.html',{'studentData':studentData, 'classes':classes,'assignments':assignments,'marks':marks,'marksDetails':marksDetails,'totalRecord':len(studentData)})