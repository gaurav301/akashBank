# Generated by Django 3.2.3 on 2021-06-05 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210605_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfers',
            name='sender_name',
            field=models.CharField(default='INVALID', max_length=200),
        ),
    ]
