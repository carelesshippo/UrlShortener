# Generated by Django 3.0.3 on 2020-09-22 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.TextField(default='a', unique=True),
            preserve_default=False,
        ),
    ]