# Generated by Django 3.1.7 on 2021-04-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_file', models.BinaryField()),
                ('name', models.TextField()),
                ('date_create', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
