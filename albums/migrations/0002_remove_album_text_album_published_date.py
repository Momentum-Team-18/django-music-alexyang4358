# Generated by Django 4.2.1 on 2023-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='text',
        ),
        migrations.AddField(
            model_name='album',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
