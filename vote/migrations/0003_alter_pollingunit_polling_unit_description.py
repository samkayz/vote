# Generated by Django 3.2.8 on 2021-10-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_alter_lga_state_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='polling_unit_description',
            field=models.TextField(null=True),
        ),
    ]