# Generated by Django 4.1.7 on 2023-04-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bongapp', '0002_rename_doctor_profile_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='review',
            field=models.CharField(max_length=525),
        ),
    ]
