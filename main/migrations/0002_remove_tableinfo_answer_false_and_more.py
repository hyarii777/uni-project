# Generated by Django 5.0.6 on 2024-05-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableinfo',
            name='answer_false',
        ),
        migrations.RemoveField(
            model_name='tableinfo',
            name='answer_true',
        ),
        migrations.AddField(
            model_name='tableinfo',
            name='is_true',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(default='', max_length=20, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('specialization', models.CharField(default='', max_length=100)),
                ('college', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('which_year', models.IntegerField(default=1)),
                ('tables', models.ManyToManyField(blank=True, related_name='students', to='main.tableinfo')),
            ],
        ),
    ]
