# Generated by Django 3.2.5 on 2021-07-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kapsoya', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_description',
            new_name='neighbourhood_description',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_location',
            new_name='neighbourhood_location',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_name',
            new_name='neighbourhood_name',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='hood_photo',
            new_name='neighbourhood_photo',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='idNo',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='profile_pic',
            new_name='profile_picture',
        ),
    ]
