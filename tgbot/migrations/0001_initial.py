# Generated by Django 5.1.1 on 2024-09-05 16:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('answer', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Chat',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=250)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('limited', models.IntegerField(default=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lasted_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
    ]
