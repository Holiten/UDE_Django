# Generated by Django 4.0.3 on 2022-03-15 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
