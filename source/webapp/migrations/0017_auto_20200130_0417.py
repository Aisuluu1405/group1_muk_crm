# Generated by Django 2.2 on 2020-01-30 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_lesson_is_saturday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='is_saturday',
            field=models.BooleanField(verbose_name='Суббота'),
        ),
    ]
