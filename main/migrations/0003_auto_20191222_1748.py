# Generated by Django 3.0.1 on 2019-12-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191222_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='staticfiles/images'),
        ),
    ]