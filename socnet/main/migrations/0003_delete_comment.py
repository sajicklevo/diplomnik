# Generated by Django 4.2.13 on 2024-08-25 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_reaction_reaction_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]