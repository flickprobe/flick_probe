# Generated by Django 4.1.4 on 2022-12-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
