from django.db import models

class Pay(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    lesson = models.ForeignKey('academy.Lesson', on_delete=models.CASCADE, verbose_name='урок', blank=True, null=True)
    course = models.ForeignKey('academy.Course', on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    price = models.FloatField(verbose_name='Сумма')
    cash = models.BooleanField(default=True, verbose_name='Наличные')


    def __str__(self):
        return f'{self.user}/{self.data}/{"Наличные" if self.data else "Картой"}'

    class Meta:
        verbose_name = 'Птатеж'
        verbose_name_plural = 'Платежи'
