# Generated by Django 2.2.5 on 2019-10-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191019_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='questiona',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
