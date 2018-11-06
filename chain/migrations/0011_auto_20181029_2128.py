# Generated by Django 2.0.5 on 2018-10-29 21:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0010_remove_faction_apikey'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targetId', models.IntegerField(default=0)),
                ('targetName', models.CharField(default='Duke', max_length=15)),
                ('result', models.CharField(default='Poutrage', max_length=15)),
                ('respect', models.FloatField(default=0)),
                ('fairFight', models.FloatField(default=0)),
                ('endDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='bonus',
            name='name',
            field=models.CharField(default='Duke', max_length=15),
        ),
        migrations.AlterField(
            model_name='count',
            name='name',
            field=models.CharField(default='Duke', max_length=15),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(default='Duke', max_length=15),
        ),
        migrations.AddField(
            model_name='target',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chain.Member'),
        ),
    ]