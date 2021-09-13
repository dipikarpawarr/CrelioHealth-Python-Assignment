"""StudentManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from StudentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home_View),
    path('stud/', include('StudentApp.urls')),
    path('register/', views.Registraion_View),
    path('addAssignment/', views.Add_Assignment_View),
    path('fillAssignmentReport/', views.Fill_Assignment_Report_View),
    path('studUpdate/<int:id>', views.Update_Student_View),
    path('updateAssignment/<int:id>', views.Update_Assignment_View),
    path('deleteAssignment/<int:id>', views.Delete_Assignment_View),
    path('deleteStudent/<int:id>', views.Delete_Student_View),
    path('allStudents/', views.AllStudents_View),
    path('allAssignments/', views.All_Assignments_View),
    path('accounts/', include('django.contrib.auth.urls')),
    path('studentReport/', views.Student_Details_View),
    path('studentAssignmentReport/<int:id>', views.Student_Report_View),
    path('dashboard/', views.Dashboard_view, name='dashboard'),
    path('data', views.Dashboard_Data, name='dashboard_data'),

]