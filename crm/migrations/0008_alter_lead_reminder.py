# Generated by Django 4.0.4 on 2022-05-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_alter_leadcomment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='reminder',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
