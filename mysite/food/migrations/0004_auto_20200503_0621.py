# Generated by Django 2.2.10 on 2020-05-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.PositiveIntegerField(),
        ),
    ]