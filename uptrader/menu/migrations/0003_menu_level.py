# Generated by Django 2.2.19 on 2023-04-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20230414_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='level',
            field=models.SmallIntegerField(null=True, verbose_name='Уровень'),
        ),
    ]
