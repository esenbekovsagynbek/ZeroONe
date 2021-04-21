from django.urls import path
from . import views

urlpatterns =[
    path("", views.CourseView.as_view()),
    path("feedback/",views.FeedBack.as_view(),name='feedback'),

]