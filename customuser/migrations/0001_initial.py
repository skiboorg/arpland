# Generated by Django 2.2.7 on 2020-02-05 09:05

import ckeditor_uploader.fields
import customuser.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('order_number', models.IntegerField(default=0, verbose_name='Порядок отображения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Эл. почта')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/', verbose_name='Фото профиля')),
                ('organization_name', models.CharField(max_length=100, null=True, verbose_name='Название организации')),
                ('organization_site', models.CharField(max_length=50, null=True, verbose_name='Сайт организации (без http)')),
                ('organization_address', models.TextField(null=True, verbose_name='Адрес организации')),
                ('organization_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание организации')),
                ('organization_avatar', models.ImageField(blank=True, upload_to='avatar/', verbose_name='Фото организации')),
                ('organization_vk', models.CharField(max_length=100, null=True, verbose_name='Ссылка на VK')),
                ('organization_fb', models.CharField(max_length=100, null=True, verbose_name='Ссылка на FB')),
                ('organization_inst', models.CharField(max_length=100, null=True, verbose_name='Ссылка на Instagram')),
                ('organization_yt', models.CharField(max_length=100, null=True, verbose_name='Ссылка на YouTube')),
                ('organization_ok', models.CharField(max_length=100, null=True, verbose_name='Ссылка на OK')),
                ('profile_ok', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', customuser.models.UserManager()),
            ],
        ),
    ]
