# Generated by Django 3.2.7 on 2021-11-09 09:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nannews', '0009_site_image_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='history',
            field=tinymce.models.HTMLField(),
        ),
    ]
