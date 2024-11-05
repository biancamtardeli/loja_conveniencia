<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns = [
   path('', IndexView.as_view(), name='index')
=======
from django.urls import path
from .views import *

urlpatterns = [
   path('', IndexView.as_view(), name='index')
>>>>>>> 0267ae72f6c0e577abe401074f101fef5c7173cc
]