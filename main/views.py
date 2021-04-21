from django.shortcuts import render
from django.views.generic import ListView
from .models import Course




class CourseView(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "main/index.html"

class FeedBack(ListView):
    model = Course
    queryset = Course.objects.all()
    template_name = "main/feedback.html"
