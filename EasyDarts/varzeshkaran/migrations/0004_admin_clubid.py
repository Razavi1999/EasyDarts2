# Generated by Django 3.2.9 on 2021-11-15 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('varzeshkaran', '0003_coach_refree'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='clubId',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='varzeshkaran.club'),
        ),
    ]
