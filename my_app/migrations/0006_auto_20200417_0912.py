# Generated by Django 3.0.2 on 2020-04-17 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_admission_addmission_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryname',
            name='cat_icon',
            field=models.ImageField(blank=True, null=True, upload_to='pic/'),
        ),
        migrations.AddField(
            model_name='university',
            name='u_icon',
            field=models.ImageField(blank=True, null=True, upload_to='pic/'),
        ),
    ]