# Generated by Django 5.1.2 on 2024-12-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Roll', models.IntegerField()),
                ('Class', models.CharField(max_length=100)),
            ],
        ),
    ]
