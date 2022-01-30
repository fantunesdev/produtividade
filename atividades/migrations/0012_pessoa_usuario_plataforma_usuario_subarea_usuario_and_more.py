# Generated by Django 4.0 on 2022-01-30 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('atividades', '0011_subarea_area_alter_atividade_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='plataforma',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='subarea',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 1, 30, 15, 6, 23, 801784, tzinfo=utc)),
        ),
    ]
