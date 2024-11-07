from django.db import models

class Course(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название курса'
    )
    image = models.ImageField(
        upload_to='school/course_images',
        blank=True,
        null=True,
        verbose_name='Превью картинка курса'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание курса'
    )

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название урока'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание урока'
    )
    image = models.ImageField(
        upload_to='school/lesson_images',
        blank=True,
        null=True,
        verbose_name='Превью картинка урока'
    )
    video_link = models.URLField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Ссылка на видео'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс'
    )


    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'