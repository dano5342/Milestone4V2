# Generated by Django 2.2.6 on 2019-11-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191101_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='c_description',
        ),
    ]
