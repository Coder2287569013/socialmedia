# Generated by Django 3.2.20 on 2023-11-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231021_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='D:\\Projects\\socialmedia\\socialmedia\\media\\NoneImage.jpg', null=True, upload_to='posts/'),
        ),
    ]