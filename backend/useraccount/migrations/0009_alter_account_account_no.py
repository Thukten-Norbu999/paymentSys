# Generated by Django 5.0.6 on 2024-06-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0008_alter_account_account_no_alter_account_qr_code_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_no',
            field=models.CharField(default='726846793', editable=False, max_length=9, unique=True),
        ),
    ]
