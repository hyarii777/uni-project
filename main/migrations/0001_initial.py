# Generated by Django 5.0.6 on 2024-05-16 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TableInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer_true', models.CharField(max_length=255)),
                ('answer_false', models.CharField(max_length=255)),
                ('table_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='main.tabletype')),
            ],
        ),
    ]