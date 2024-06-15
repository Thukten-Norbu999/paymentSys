# Generated by Django 5.0.6 on 2024-06-15 17:12

import transaction.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('frm', models.CharField(max_length=9, verbose_name='From account')),
                ('to', models.CharField(max_length=9, verbose_name='To account')),
                ('remarks', models.CharField(max_length=250, verbose_name='Remarks')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date-Time of Transaction')),
                ('journalNo', models.CharField(default=transaction.models.gen_journalNumber, max_length=12, unique=True, verbose_name='Journal Number')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]