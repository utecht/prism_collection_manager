# Generated by Django 3.1.1 on 2020-09-21 17:40

from django.db import migrations, models
import trix.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', trix.fields.TrixField(verbose_name='Content')),
            ],
        ),
    ]
