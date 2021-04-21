from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.


class Course(models.Model):
    """Курс"""
    name = models.CharField("Курс", max_length=200)
    created = models.DateTimeField(auto_now=True)
    descriptions = models.TextField(null=True,blank=True)
    price = models.IntegerField("Стоимость",default = 7000)
    image = models.ImageField(upload_to = "images")
    draft = models.BooleanField(default=False)
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"    

class Enroll(models.Model):
    """Регистрация"""
    name = models.CharField("Регистрация", max_length = 200)
    last_name = models.CharField("Фамилия", max_length = 200)
    phone_number = models.CharField("Номер", max_length = 200)
    email = models.CharField("Адрес", max_length = 200)
    courses_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрация"


class Events(models.Model):

     name = models.CharField("Мероприятия", max_length = 200)
     descriptions = models.TextField(null=True,blank=True)
     due = models.DateTimeField(auto_now=True)
     created_date = models.DateTimeField(auto_now=True)
     main_image = models.ImageField(upload_to="images")
     images = models.ImageField(upload_to="images")
     

     def __str__(self):
          return self.name

     class Meta:
         verbose_name = "Мероприятия"  
         verbose_name_plural = "Мероприятия"


class FeedBack(models.Model):
    name = models.CharField("Отзыв", max_length = 200)
    descriptions = models.TextField(null=True,blank=True)


    def __str__(self):
         return self.name

    class Meta:
        verbose_name = "Отзыв"  
        verbose_name_plural = "Отзыв"



             
