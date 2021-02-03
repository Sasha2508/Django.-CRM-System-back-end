from django.urls import path
from .views import *

urlpatterns = [
    path('list/', GetClientList.as_view()),
    path('create/', CreateClient.as_view())


]