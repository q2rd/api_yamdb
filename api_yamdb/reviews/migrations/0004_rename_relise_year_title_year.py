# Generated by Django 3.2 on 2023-05-16 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_title_relise_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='relise_year',
            new_name='year',
        ),
    ]
