# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import library_sys.models
import library_sys.validators


class Migration(migrations.Migration):

    dependencies = [
        ('library_sys', '0008_auto_20170319_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, height_field='cover_height', help_text='Selecione a imagem de capa\n                               do livro, normalmente nos formatos\n                               jpg, png, gif, etc.', null=True, upload_to=library_sys.models.Book.get_upload_to_image, verbose_name='capa', width_field='cover_width'),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, help_text='Selecione o arquivo do livro\n                             para download, normalmente nos formatos\n                             pdf, epub, etc.', null=True, upload_to=library_sys.models.Book.get_upload_to_file, validators=library_sys.validators.FileValidator(allowed_mimetypes=('application/pdf', 'application/epub+zip'), max_size=5242880), verbose_name='arquivo'),
        ),
    ]