from django.db import models


class Courses(models.Model):
    """Курсы"""
    name = models.CharField("Имя курса", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="images/")
    price = models.PositiveIntegerField("Стоимость", default=7000,
                                        help_text="указывать сумму в сомах")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
