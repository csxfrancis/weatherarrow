# Generated by Django 3.1.3 on 2020-12-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_auto_20201129_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='feeltemp',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]