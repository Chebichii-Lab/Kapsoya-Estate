# Generated by Django 3.2.5 on 2021-07-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapsoya', '0006_auto_20210725_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Security'), ('2', 'Health Emergency'), ('3', 'Entertainment'), ('4', 'Fire Breakouts'), ('5', 'Playground'), ('6', 'Death'), ('7', 'Gym')], max_length=120),
        ),
    ]
