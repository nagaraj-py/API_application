# Generated by Django 3.1.6 on 2022-02-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_empdata_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('number', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('0', 'male'), ('1', 'female'), ('2', 'not specified')], max_length=10)),
                ('company', models.CharField(max_length=50)),
                ('emp_id', models.IntegerField()),
                ('manager', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Empdata',
        ),
    ]
