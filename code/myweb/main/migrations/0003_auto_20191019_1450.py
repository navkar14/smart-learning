# Generated by Django 2.2.3 on 2019-10-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191010_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.AddField(
            model_name='quiz',
            name='ques_slug',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AddField(
            model_name='quiz',
            name='questiona',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AddField(
            model_name='quiz',
            name='questionb',
            field=models.CharField(default=1, max_length=200),
        ),
    ]