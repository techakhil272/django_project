# Generated by Django 4.0.1 on 2022-01-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
