# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-23 19:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('exp_date', models.DateTimeField(verbose_name='Expiry Date')),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(to='main.Course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=main.models.upload_path)),
                ('pub_date', models.DateTimeField(verbose_name='Date Published')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Course')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=140)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('section_number', models.IntegerField()),
                ('course', models.ManyToManyField(to='main.Course')),
            ],
        ),
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=5)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Department')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='studyfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StudyField'),
        ),
        migrations.AddField(
            model_name='material',
            name='section',
            field=models.ManyToManyField(to='main.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='studyfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.StudyField'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lecturer'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='section',
            field=models.ManyToManyField(to='main.Section'),
        ),
    ]