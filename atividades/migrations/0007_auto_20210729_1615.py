# Generated by Django 3.2.5 on 2021-07-29 19:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0006_auto_20210727_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='usuario',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 7, 29, 19, 15, 33, 787887, tzinfo=utc)),
        ),
    ]