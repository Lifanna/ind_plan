# Generated by Django 3.1.7 on 2021-05-13 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Educational work type')),
            ],
            options={
                'verbose_name': 'Educational work type',
                'verbose_name_plural': 'Educational work types',
            },
        ),
        migrations.CreateModel(
            name='EduMethodWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Educational methodical work type')),
            ],
            options={
                'verbose_name': 'Educational methodical work type',
                'verbose_name_plural': 'Educational methodical work types',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Specialty name')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
            },
        ),
        migrations.CreateModel(
            name='EduMethodWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_1', models.IntegerField(blank=True, verbose_name='Hours count')),
                ('by_plan', models.IntegerField(blank=True, verbose_name='Plan')),
                ('by_fact', models.IntegerField(blank=True, verbose_name='Fact')),
                ('edu_method_work_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu_work.edumethodworktype', verbose_name='Educational methodical work type')),
                ('specialty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu_work.specialty', verbose_name='Specialty')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Educational work',
                'verbose_name_plural': 'Educational works',
            },
        ),
        migrations.CreateModel(
            name='EducationalWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_plan_1', models.IntegerField(blank=True, verbose_name='Plan 1 semester')),
                ('by_fact_1', models.IntegerField(blank=True, verbose_name='Fact 1 semester')),
                ('deviation_1', models.IntegerField(blank=True, verbose_name='Deviation 1 semester')),
                ('by_plan_2', models.IntegerField(blank=True, verbose_name='Plan 2 semester')),
                ('by_fact_2', models.IntegerField(blank=True, verbose_name='Fact 2 semester')),
                ('deviation_2', models.IntegerField(blank=True, verbose_name='Deviation 2 semester')),
                ('by_plan_annual', models.IntegerField(blank=True, verbose_name='Plan annual')),
                ('by_fact_annual', models.IntegerField(blank=True, verbose_name='Fact annual')),
                ('deviation_annual', models.IntegerField(blank=True, verbose_name='Deviation annual')),
                ('education_work_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu_work.educationalworktype', verbose_name='Educational work type')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Educational work',
                'verbose_name_plural': 'Educational works',
            },
        ),
    ]
