# Generated by Django 4.2.1 on 2023-05-25 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_remove_album_published_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
