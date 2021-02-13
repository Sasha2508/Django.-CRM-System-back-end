from django.urls import path
from .views import *

urlpatterns = [
    path('list/', GetEmployeeList.as_view()),
    path('create/', CreateEmployee.as_view()),
    path('type/list/', GetToDoTypeList.as_view()),
    path('type/create/', CreateToDoType.as_view()),
    path('todo/list/', GetToDoList.as_view()),
    path('todo/create/', CreateToDo.as_view()),
    path('department/list/', GetDepartmentList.as_view()),
    path('department/create/', CreateDepartment.as_view())

]