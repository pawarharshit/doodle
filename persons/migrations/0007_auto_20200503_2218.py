# Generated by Django 3.0.5 on 2020-05-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0006_auto_20200503_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='persons/photos/profile_images/default_pic.png', upload_to='persons/photos/profile_images'),
        ),
    ]