from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    preview = models.ImageField(verbose_name='Фото', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} {self.description[:15]}...'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
