# Generated by Django 2.0.3 on 2018-04-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twilio_mgr', '0021_auto_20180412_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagelog',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='messagelog',
            name='sms_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
