# Generated by Django 4.0.5 on 2022-06-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorsitems',
            name='item_id',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
