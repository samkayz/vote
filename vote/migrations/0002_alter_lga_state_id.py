# Generated by Django 3.2.8 on 2021-10-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lga',
            name='state_id',
            field=models.BigIntegerField(),
        ),
    ]
