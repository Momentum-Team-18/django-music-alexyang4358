# Generated by Django 4.2.1 on 2023-05-23 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_remove_album_text_album_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='published_date',
        ),
    ]
