# Generated by Django 3.0.2 on 2020-01-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dono', '0002_dono_telefone'),
        ('gatinho', '0004_auto_20200110_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatinho',
            name='dono',
            field=models.ManyToManyField(blank=True, to='dono.Dono'),
        ),
    ]
