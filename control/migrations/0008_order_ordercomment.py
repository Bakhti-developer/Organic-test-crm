# Generated by Django 4.0.3 on 2022-04-11 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_remove_ordercomment_account_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.IntegerField(default=1)),
                ('date_process_1', models.DateTimeField(auto_now_add=True)),
                ('date_process_2', models.DateTimeField(blank=True, null=True)),
                ('date_process_3', models.DateTimeField(blank=True, null=True)),
                ('date_process_4', models.DateTimeField(blank=True, null=True)),
                ('date_process_5', models.DateTimeField(blank=True, null=True)),
                ('date_process_6', models.DateTimeField(blank=True, null=True)),
                ('date_process_7', models.DateTimeField(blank=True, null=True)),
                ('date_process_8', models.DateTimeField(blank=True, null=True)),
                ('social', models.CharField(max_length=255)),
                ('fio', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.course')),
            ],
        ),
        migrations.CreateModel(
            name='OrderComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.account')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.order')),
            ],
        ),
    ]
