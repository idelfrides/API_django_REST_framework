# Generated by Django 2.2.6 on 2019-10-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191009_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
