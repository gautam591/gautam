# Generated by Django 3.0.8 on 2020-11-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axisPosts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'female'), ('3', 'others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'female'), ('3', 'others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='recipt',
            field=models.ImageField(blank=True, null=True, upload_to='gautam/'),
        ),
    ]
