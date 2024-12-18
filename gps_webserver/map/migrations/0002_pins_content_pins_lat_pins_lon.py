# Generated by Django 5.1.3 on 2024-12-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pins',
            name='content',
            field=models.CharField(default='helloWorld', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pins',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pins',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]