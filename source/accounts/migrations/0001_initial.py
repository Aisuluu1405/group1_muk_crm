# Generated by Django 2.2 on 2019-12-26 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('phone_number', phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='Номер телеофона')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('address_fact', models.CharField(max_length=100, verbose_name='Фактический Адрес')),
                ('parent_one', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='parent_one', to=settings.AUTH_USER_MODEL, verbose_name='Родитель Один')),
                ('parent_two', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='parent_two', to=settings.AUTH_USER_MODEL, verbose_name='Родитель Два')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
