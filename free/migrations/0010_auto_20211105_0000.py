# Generated by Django 3.2.6 on 2021-11-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0009_auto_20211104_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='execution',
            name='queue_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='execution',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
