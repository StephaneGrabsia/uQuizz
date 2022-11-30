# Generated by Django 4.1.2 on 2022-11-30 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='room_url',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='subject',
        ),
        migrations.AddField(
            model_name='exercise',
            name='statement',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='teacher_admin', to='api.member'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='correct_output',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='solution',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='output',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='source',
            field=models.TextField(null=True),
        ),
    ]
