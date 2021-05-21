from django.urls import path
from opensource import views

urlpatterns = [
    path('', views.getAllStudents),
    path('home/', views.home),
    path('student/<studentId>', views.getStudent),
    path('new/', views.newStudent),
    path('edit/<studentId>', views.editStudent),
    path('delete/<studentId>', views.deleteStudent),
]   