# Generated by Django 5.0.4 on 2024-06-04 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creamsQuizz', '0006_remove_waffel_cakes_remove_waffel_icecream_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waffel',
            old_name='icecream',
            new_name='scoops',
        ),
    ]
