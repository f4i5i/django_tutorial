# Generated by Django 3.1.3 on 2020-12-01 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201201_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_paosted',
            new_name='date_posted',
        ),
    ]
