from django.urls import path
from .views import *

urlpatterns = [
    path('brands/list/', GetBrandList.as_view()),
    path('cars/list/', GetCarList.as_view())

]