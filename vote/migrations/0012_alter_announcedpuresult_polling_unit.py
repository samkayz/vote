# Generated by Django 3.2.8 on 2021-10-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0011_alter_agentname_polling_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcedpuresult',
            name='polling_unit',
            field=models.BigIntegerField(),
        ),
    ]