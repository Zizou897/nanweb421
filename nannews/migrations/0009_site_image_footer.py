# Generated by Django 3.2.7 on 2021-10-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nannews', '0008_auto_20211001_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='image_footer',
            field=models.FileField(default=1, upload_to='image_foot'),
            preserve_default=False,
        ),
    ]