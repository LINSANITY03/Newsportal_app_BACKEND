# Generated by Django 4.2.6 on 2023-10-28 12:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientside', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' '),
        ),
    ]