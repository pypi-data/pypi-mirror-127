# Generated by Django 3.1.7 on 2021-07-26 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0153_auto_20210723_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('first_name', 'last_name')},
        ),
    ]
