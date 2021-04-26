import datetime
from django.shortcuts import render
from .models import Courses


today = datetime.datetime.now()
month = today.strftime("%B")
year = today.strftime("%Y")


def home(request):
    courses = Courses.objects.all()
    print(courses[0].image.url)
    return render(request, 'main/index.html', {
        'courses': courses
    })


