from django.urls import path
from .views import landing1, landing2

urlpatterns = [
    path('', landing1, name='landing1'),
    path('step2/', landing2, name='landing2'),
]