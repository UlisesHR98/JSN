# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-01 16:30


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_generatedreports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedreports',
            name='order',
        ),
        migrations.DeleteModel(
            name='GeneratedReports',
        ),
    ]
