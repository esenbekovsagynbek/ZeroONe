from django.shortcuts import render
from .models import Courses


def home(request):
    courses = Courses.objects.all()
    return render(request, 'main/index.html', {
        'courses': courses
    })
