# Generated by Django 4.0.4 on 2022-05-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_order_city_order_email_order_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='Bishkek', max_length=50, null=True),
        ),
    ]
