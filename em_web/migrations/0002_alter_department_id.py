# Generated by Django 5.1.1 on 2024-11-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('em_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='部门id'),
        ),
    ]
