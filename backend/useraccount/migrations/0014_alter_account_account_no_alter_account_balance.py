# Generated by Django 5.0.6 on 2024-06-17 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0013_alter_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(default='204045867', editable=False, max_length=9, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]
