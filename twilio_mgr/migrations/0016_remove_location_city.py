# Generated by Django 2.0.3 on 2018-04-04 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_mgr', '0015_auto_20180404_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
    ]
