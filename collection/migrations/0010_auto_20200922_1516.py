# Generated by Django 3.1.1 on 2020-09-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20200922_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='download',
            name='nbia_search',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='downloadversion',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]