# Generated by Django 3.0.8 on 2020-12-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(default='NULL', max_length=20)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(default='NULL', max_length=2000)),
                ('link', models.CharField(default='NULL', max_length=200)),
                ('seminarpopularity', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['seminarpopularity'],
            },
        ),
    ]
