# Generated by Django 4.2 on 2023-04-04 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OtpCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('code', models.PositiveSmallIntegerField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
