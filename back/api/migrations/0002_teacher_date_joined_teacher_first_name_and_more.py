# Generated by Django 4.1.2 on 2022-12-20 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 20, 23, 53, 6, 526327, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(default='toto', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('Femme', 'F'), ('Homme', 'M')], default='Femme', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(default='tata', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='djadja', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='mama', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]