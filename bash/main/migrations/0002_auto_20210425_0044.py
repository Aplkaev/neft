# Generated by Django 3.1.7 on 2021-04-24 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_create', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='modelfile',
            name='name',
        ),
        migrations.CreateModel(
            name='ModelArticleFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelarticle')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelfile')),
            ],
        ),
    ]
