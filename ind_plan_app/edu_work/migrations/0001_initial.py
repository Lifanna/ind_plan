# Generated by Django 3.1.7 on 2021-04-05 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by_plan_1', models.IntegerField(blank=True, verbose_name='План 1 семестр')),
                ('by_fact_1', models.IntegerField(blank=True, verbose_name='Факт 1 семестр')),
                ('deviation_1', models.IntegerField(blank=True, verbose_name='Отклонение 1 семестр')),
                ('by_plan_2', models.IntegerField(blank=True, verbose_name='План 2 семестр')),
                ('by_fact_2', models.IntegerField(blank=True, verbose_name='Факт 2 семестр')),
                ('deviation_2', models.IntegerField(blank=True, verbose_name='Отклонение 2 семестр')),
                ('by_plan_annual', models.IntegerField(blank=True, verbose_name='План за год')),
                ('by_fact_annual', models.IntegerField(blank=True, verbose_name='Факт за год')),
                ('deviation_annual', models.IntegerField(blank=True, verbose_name='Отклонение за год')),
                ('education_work_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu_work.educationalworktype')),
            ],
        ),
    ]
