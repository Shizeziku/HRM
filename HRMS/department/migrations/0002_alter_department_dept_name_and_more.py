# Generated by Django 4.2 on 2025-01-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Dept_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
