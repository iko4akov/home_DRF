from django.db import models

class Pay(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True)

    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course_lesson = models.ForeignKey('academy.Course', on_delete=models.CASCADE, verbose_name='Курс или урок')
    price = models.FloatField(verbose_name='Сумма')
    cash = models.BooleanField(default=True, verbose_name='Наличные')

    def __str__(self):
        return f'{self.user}/{self.data}/{"Наличные" if self.data else "Картой"}'

    class Meta:
        verbose_name = 'Птатеж'
        verbose_name_plural = 'Платежи'
        ordering = ('price',)
