# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-03 03:28


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statereport', '0016_auto_20170319_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='debt_comments',
            field=models.CharField(max_length=55),
        ),
    ]