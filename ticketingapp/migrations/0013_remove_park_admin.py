# Generated by Django 2.1.4 on 2018-12-24 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketingapp', '0012_rename_mall_to_park'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='admin',
        ),
    ]
