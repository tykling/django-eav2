# Generated by Django 2.2.6 on 2019-10-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0009_auto_20191027_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='generic_value_uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]