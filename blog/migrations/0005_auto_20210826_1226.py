# Generated by Django 3.2.6 on 2021-08-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210826_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='extension',
        ),
        migrations.AddField(
            model_name='game',
            name='is_extension',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='has_extension',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Extension',
        ),
    ]
