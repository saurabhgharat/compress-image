# Generated by Django 2.0.2 on 2018-12-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compress', '0006_auto_20181203_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='get_image_path'),
        ),
    ]
