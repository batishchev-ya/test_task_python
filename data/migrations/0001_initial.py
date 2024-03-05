# Generated by Django 3.2.24 on 2024-02-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('user_agent', models.CharField(max_length=200)),
                ('accept_language', models.CharField(max_length=200)),
            ],
        ),
    ]