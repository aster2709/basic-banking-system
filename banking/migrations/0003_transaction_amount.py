# Generated by Django 3.1.7 on 2021-02-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]