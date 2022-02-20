# Generated by Django 3.1.6 on 2021-12-13 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.CharField(blank=True, max_length=8000, null=True)),
                ('type', models.CharField(choices=[('academic', 'academic'), ('non-academic', 'non-academic')], max_length=100)),
                ('edition', models.CharField(max_length=512)),
                ('author', models.CharField(max_length=1024)),
                ('publisher', models.CharField(max_length=1024)),
                ('file', models.FileField(upload_to='books')),
                ('cover', models.ImageField(default='bookdefault.png', upload_to='book_cover')),
            ],
        ),
        migrations.CreateModel(
            name='BookAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_views', models.IntegerField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elibrary.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField()),
                ('reviews', models.IntegerField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='elibrary.book')),
            ],
        ),
        migrations.CreateModel(
            name='TextReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.bookreview')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.bookreview')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='custom_user.organization')),
            ],
        ),
        migrations.CreateModel(
            name='BookAnalyticViewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_time', models.DateTimeField(auto_now=True)),
                ('book_analytics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.bookanalytics')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.library'),
        ),
    ]