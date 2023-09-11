# Generated by Django 4.2.5 on 2023-09-11 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0004_alter_lesson_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')),
                ('price', models.FloatField(verbose_name='Сумма')),
                ('cash', models.BooleanField(default=True, verbose_name='Наличные')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='academy.lesson', verbose_name='урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Птатеж',
                'verbose_name_plural': 'Платежи',
                'ordering': ('price',),
            },
        ),
    ]