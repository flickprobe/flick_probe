# Generated by Django 4.1.4 on 2022-12-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=100)),
                ('cast', models.CharField(max_length=800)),
                ('description', models.TextField(max_length=5000)),
                ('release_date', models.DateField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
