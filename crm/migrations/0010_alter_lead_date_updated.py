# Generated by Django 4.0.4 on 2022-05-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_lead_droped_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
