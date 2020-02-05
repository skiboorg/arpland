# Generated by Django 2.2.7 on 2020-02-05 09:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Название ')),
                ('name_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='blog_img/', verbose_name='Изображение превью (555 x 390)')),
                ('page_h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег H1')),
                ('page_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название страницы SEO')),
                ('page_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание страницы SEO')),
                ('page_keywords', models.TextField(null=True, verbose_name='Keywords SEO')),
                ('short_description', models.CharField(blank=True, max_length=200, verbose_name='Краткое описание ')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Текст новости')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотров')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Отображать статью ?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]