# Generated by Django 2.2.2 on 2019-06-18 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_fundraising', '0014_auto_20190615_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundraiser',
            name='email',
        ),
    ]
