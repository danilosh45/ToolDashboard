# Generated by Django 2.1.7 on 2019-03-29 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_scrape',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
