# Generated by Django 4.1 on 2022-08-29 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_author', models.SmallIntegerField(default=0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.CharField(choices=[('NW', 'Новость'), ('AR', 'Статья')], default='AR', max_length=2)),
                ('some_data', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('rating_pt', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='News.PostCategory', to='News.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('some_data_cm', models.DateTimeField(auto_now_add=True)),
                ('rating_cm', models.SmallIntegerField(default=0)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]