from django.urls import path
from .views import resume, index

urlpatterns = [
    path('', index, name='index'),
    path('resume/', resume, name='resume'),
]
