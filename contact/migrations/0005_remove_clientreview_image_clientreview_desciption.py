# Generated by Django 5.0.4 on 2024-09-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_clientreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientreview',
            name='image',
        ),
        migrations.AddField(
            model_name='clientreview',
            name='desciption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
