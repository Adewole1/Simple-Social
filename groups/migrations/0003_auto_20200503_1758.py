# Generated by Django 3.0.5 on 2020-05-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.CharField(default='', max_length=500),
        ),
    ]