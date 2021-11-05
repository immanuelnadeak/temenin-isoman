# Generated by Django 3.2.8 on 2021-11-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipsAndTrick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('source', models.CharField(max_length=500)),
                ('published_date', models.DateField()),
                ('brief_description', models.TextField()),
                ('image_url', models.CharField(max_length=500)),
                ('article_url', models.CharField(max_length=500)),
            ],
        ),
    ]
