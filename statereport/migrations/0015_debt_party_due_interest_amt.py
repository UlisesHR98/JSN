# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-15 03:20


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statereport', '0014_auto_20170226_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='party_due_interest_amt',
            field=models.CharField(default='0000000000{', max_length=50),
            preserve_default=False,
        ),
    ]