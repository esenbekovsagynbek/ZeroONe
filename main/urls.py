from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("courses/<int:pk>/", views.courses, name='courses'),
]