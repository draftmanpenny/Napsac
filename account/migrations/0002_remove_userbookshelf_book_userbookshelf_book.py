# Generated by Django 4.1 on 2022-10-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbookshelf',
            name='book',
        ),
        migrations.AddField(
            model_name='userbookshelf',
            name='book',
            field=models.ManyToManyField(to='account.book'),
        ),
    ]
