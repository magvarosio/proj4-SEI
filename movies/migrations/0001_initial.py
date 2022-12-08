# Generated by Django 4.1.4 on 2022-12-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField(default=False)),
                ('backdrop_path', models.CharField(max_length=5000)),
                ('original_language', models.CharField(max_length=5000)),
                ('original_title', models.CharField(max_length=5000)),
                ('overview', models.CharField(max_length=5000)),
                ('popularity', models.FloatField()),
                ('poster_path', models.CharField(max_length=5000)),
                ('release_date', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=100)),
                ('video', models.BooleanField(default=False)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.PositiveBigIntegerField()),
                ('genre_ids', models.ManyToManyField(related_name='movies', to='genres.genre')),
            ],
        ),
    ]
