# Generated by Django 3.2.8 on 2021-10-15 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('green_branchs', '0009_auto_20211015_0312'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry_sched',
        ),
        migrations.DeleteModel(
            name='Topic_sched',
        ),
    ]
