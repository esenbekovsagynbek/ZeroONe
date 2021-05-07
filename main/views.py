import datetime
from django.shortcuts import render
from .models import *

today = datetime.datetime.now()
month = today.strftime("%B")
year = today.strftime("%Y")


def home(request):
    course = Courses.objects.all()
    feedbacks = Feedbacks.objects.all()
    return render(request, 'main/index.html', {
        'courses': course,
        'feedbacks': feedbacks,
    })


def courses(request, pk):
    course = Courses.objects.get(id=pk)
    return render(request, 'main/courses.html', {
        'course': course,
    })
