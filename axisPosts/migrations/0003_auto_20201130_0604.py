# Generated by Django 3.0.8 on 2020-11-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axisPosts', '0002_auto_20201130_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'female'), ('Others', 'others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='apply',
            name='hobby',
            field=models.CharField(choices=[('Drawing', 'singing'), ('Swimming', 'swimming'), ('Dancing', 'Dancing'), ('Reading', 'reading')], max_length=20),
        ),
        migrations.AlterField(
            model_name='apply',
            name='mobile',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='apply',
            name='qualifications',
            field=models.CharField(choices=[('High School', 'High School'), ('Higher school', 'higher school'), ('Bachelors', 'Bachelors'), ('P.H.D', 'P.H.D')], max_length=30),
        ),
        migrations.AlterField(
            model_name='apply',
            name='subject',
            field=models.CharField(choices=[('Computer Science', 'Computer science'), ('MBA', 'MBA'), ('BBA', 'BBA'), ('civil Engineer', 'CIvil Engineer')], max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'female'), ('Others', 'others')], max_length=10),
        ),
    ]
