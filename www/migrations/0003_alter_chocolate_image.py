# Generated by Django 4.0.4 on 2022-05-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_chocolate_description_chocolate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='image',
            field=models.ImageField(height_field=600, null=True, upload_to='C:\\Users\\Kalyibek\\PycharmProjects\\Samat\\media\\images', width_field=400),
        ),
    ]
