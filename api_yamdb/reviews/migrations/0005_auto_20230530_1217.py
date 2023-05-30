# Generated by Django 3.2 on 2023-05-30 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_rename_reviw_comment_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',)},
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_GenreTitle', to='reviews.genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='genretitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_GenreTitle', to='reviews.title', verbose_name='Произведение'),
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(default='Категория не выбрана.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='reviews.category', verbose_name='Категория произведения.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user')], default='user', max_length=50),
        ),
    ]