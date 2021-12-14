# Generated by Django 4.0 on 2021-12-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_musician_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
