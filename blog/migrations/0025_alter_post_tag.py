# Generated by Django 5.0.4 on 2024-06-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, default='Travel', max_length=50, null=True),
        ),
    ]
