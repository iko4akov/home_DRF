from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.EmailField(verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description[:15]}...'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
