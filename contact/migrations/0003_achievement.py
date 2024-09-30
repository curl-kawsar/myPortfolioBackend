# Generated by Django 5.0.4 on 2024-09-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
