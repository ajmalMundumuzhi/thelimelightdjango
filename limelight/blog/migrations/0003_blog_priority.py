# Generated by Django 5.0.7 on 2024-07-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
