# Generated by Django 3.2.3 on 2021-06-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='cust_email',
            field=models.CharField(default='noemail@example.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='customers',
            name='cust_id',
            field=models.IntegerField(),
        ),
    ]
