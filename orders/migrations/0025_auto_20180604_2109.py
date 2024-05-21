# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-05 01:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_generatedreport_docket_list_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='addr1',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='addr2',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='zip',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]