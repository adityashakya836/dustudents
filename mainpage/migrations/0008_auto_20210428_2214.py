# Generated by Django 3.1.4 on 2021-04-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20210419_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=250),
        ),
    ]
