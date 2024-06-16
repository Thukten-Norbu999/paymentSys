# Generated by Django 5.0.6 on 2024-06-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_alter_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(default='109939024', editable=False, max_length=9, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('user', 'account_no')},
        ),
    ]
