# Generated by Django 4.2 on 2023-04-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bejegyzes',
            name='allapot',
            field=models.CharField(choices=[('Jóvahagyásra vár', 'Jóvahagyásra vár'), ('Jóváhagyott', 'Jóváhagyott')], default='Jóváhagyásra vár', max_length=30, verbose_name='Állapot'),
        ),
    ]
