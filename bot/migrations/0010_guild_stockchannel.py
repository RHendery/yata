# Generated by Django 2.2.7 on 2019-12-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_guild_managechannels'),
    ]

    operations = [
        migrations.AddField(
            model_name='guild',
            name='stockChannel',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
    ]
