# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-25 16:52


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacerscraper', '0015_pacerjudgmentparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacerJudgmentAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias_name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='pacerjudgmentindexcase',
            name='alias_file_processed',
            field=models.CharField(db_index=True, default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='pacerjudgmentindexcase',
            name='party_file_processed',
            field=models.CharField(db_index=True, default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='pacerjudgmentalias',
            name='judgment_index_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacerscraper.PacerJudgmentIndexCase'),
        ),
    ]