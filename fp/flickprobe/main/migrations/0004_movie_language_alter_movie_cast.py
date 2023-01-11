# Generated by Django 4.1.4 on 2023-01-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_movie_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('1', 'Hindi'), ('2', 'English')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.CharField(max_length=800),
        ),
    ]