# Generated by Django 3.1 on 2020-09-12 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axisPosts', '0008_auto_20200912_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postimage',
            new_name='postImage',
        ),
    ]
