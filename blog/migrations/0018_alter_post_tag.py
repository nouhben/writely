# Generated by Django 5.0.4 on 2024-06-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, default='Culture', max_length=50, null=True),
        ),
    ]
