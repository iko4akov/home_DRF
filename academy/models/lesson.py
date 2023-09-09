from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.EmailField(verbose_name='Фото')
    video = models.URLField(verbose_name='Видео')

    course = models.ForeignKey('academy.Course', on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f'{self.name} {self.description[:15]}..., {self.course}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
