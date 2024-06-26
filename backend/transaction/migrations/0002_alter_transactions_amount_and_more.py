# Generated by Django 5.0.6 on 2024-06-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.FloatField(verbose_name='Amount'),
        ),
        migrations.AddConstraint(
            model_name='transactions',
            constraint=models.UniqueConstraint(fields=('id', 'journalNo'), name='unique_transaction'),
        ),
    ]
