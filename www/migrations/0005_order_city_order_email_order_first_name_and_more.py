# Generated by Django 4.0.4 on 2022-05-29 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_alter_chocolate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(choices=[('Aydarken', 'aidarken'), ('Balykchy', 'balykcy'), ('Batken', 'batken'), ('Bazar-Korgon', 'bazar'), ('Bishkek', 'bish'), ('Cholpon-Ata', 'ch-a'), ('Jalal-Abad', 'jalal-abad'), ('Kant', 'kant'), ('Karakol', 'karakol'), ('Kemin', 'kemin'), ('Naryn', 'naryn'), ('Osh', 'osh'), ('Talas', 'talas'), ('Tokmok', 'tokmok')], default='Bishkek', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
