# Generated by Django 4.0 on 2022-02-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=200, null=True),
        ),
    ]