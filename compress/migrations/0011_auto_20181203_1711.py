# Generated by Django 2.0.2 on 2018-12-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compress', '0010_auto_20181203_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
