from django.contrib import admin
from .models import (Course,Enroll,Events,FeedBack)

admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Events)
admin.site.register(FeedBack)