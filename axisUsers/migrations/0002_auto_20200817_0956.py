# Generated by Django 3.1 on 2020-08-17 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axisUsers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='axisAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awardName', models.CharField(max_length=20)),
                ('awardType', models.IntegerField(default=0)),
                ('awardDesc', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='userAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('awardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axisUsers.axisawards')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Awards',
        ),
    ]
