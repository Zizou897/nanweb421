# Generated by Django 3.2.7 on 2021-09-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nannews', '0006_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='history',
            field=models.TextField(),
        ),
    ]
