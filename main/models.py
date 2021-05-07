from django.db import models


class Courses(models.Model):
    """Курсы"""
    name = models.CharField("Имя курса", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="images/")
    price = models.PositiveIntegerField("Стоимость", default=7000,
                                        help_text="указывать сумму в сомах")
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Feedbacks(models.Model):
    """Отзывы"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Отзыв")
    course = models.ForeignKey(
        Courses, verbose_name="Курс", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Events(models.Model):
    """Мероприятие"""
    title = models.CharField("Имя", max_length=200)
    description = models.TextField("Описание")
    due_on = models.DateField("Дата выполнения", blank=True)
    teacher_name = models.CharField("Имя преподавателя", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
