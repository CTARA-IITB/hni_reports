# Generated by Django 3.2.11 on 2022-01-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20220103_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
