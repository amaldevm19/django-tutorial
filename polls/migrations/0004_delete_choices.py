# Generated by Django 3.0 on 2020-02-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choices',
        ),
    ]