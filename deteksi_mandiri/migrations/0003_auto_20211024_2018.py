# Generated by Django 3.2.7 on 2021-10-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deteksi_mandiri', '0002_auto_20211024_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='score',
        ),
        migrations.AddField(
            model_name='answer',
            name='poin',
            field=models.IntegerField(default=0, help_text='Poin for each answer'),
            preserve_default=False,
        ),
    ]
