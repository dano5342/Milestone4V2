# Generated by Django 2.2.6 on 2019-11-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_sold_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
