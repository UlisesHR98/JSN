# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-27 00:39


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statereport', '0012_auto_20170226_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='party_type_indicator_party',
            field=models.CharField(max_length=50),
        ),
    ]
