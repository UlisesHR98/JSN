# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-21 20:38


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JudgmentIndexReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('archive_file', models.CharField(max_length=255)),
            ],
        ),
    ]