# Generated by Django 4.0.3 on 2022-04-11 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_remove_category_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.discount'),
        ),
    ]
