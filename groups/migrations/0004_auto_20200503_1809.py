# Generated by Django 3.0.5 on 2020-05-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20200503_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.CharField(default='', editable=False, max_length=500),
        ),
    ]