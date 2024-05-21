# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-26 23:30


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statereport', '0008_debt_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statereport.Case'),
        ),
    ]