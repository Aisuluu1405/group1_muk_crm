# Generated by Django 2.2 on 2020-02-28 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_journalnote_group_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalnote',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='note_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Кем создана'),
        ),
        migrations.AlterField(
            model_name='journalnote',
            name='theme',
            field=models.CharField(max_length=100, verbose_name='Тема или название занятия'),
        ),
    ]
