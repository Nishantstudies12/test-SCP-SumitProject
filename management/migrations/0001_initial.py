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
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1024)),
                ('url', models.URLField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('max_marks', models.IntegerField(blank=True, null=True)),
                ('problem', models.FileField(blank=True, null=True, upload_to='assignment/problem')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=255)),
                ('c_description', models.CharField(max_length=512)),
                ('c_status', models.BooleanField(default=False)),
                ('for_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('for_room', models.ManyToManyField(to='custom_user.Room')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='custom_user.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='LiveSessionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=2048, null=True)),
                ('status', models.CharField(choices=[('accepted', 'accepted'), ('requested', 'requested'), ('rejected', 'rejected')], default='requested', max_length=50)),
                ('scheduled_time', models.DateTimeField(blank=True, null=True)),
                ('webrtc_offer', models.CharField(blank=True, max_length=500000, null=True)),
                ('webrtc_answer', models.CharField(blank=True, max_length=500000, null=True)),
                ('for_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
                ('for_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_user.teacher')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_user.student')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.CharField(blank=True, default='default', max_length=512, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('type', models.CharField(choices=[('rtc', 'rtc'), ('3rd party', '3rd party')], max_length=100)),
                ('session_id', models.CharField(blank=True, max_length=500, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.course')),
                ('web_rtc_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.livesessionrequest')),
            ],
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('enable', 'enable'), ('disable', 'disable')], max_length=100)),
                ('room', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_user.room')),
                ('slot', models.ManyToManyField(to='management.Slot')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.FileField(upload_to='assignment/solution')),
                ('marks', models.IntegerField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=512, null=True)),
                ('solution_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.assignment')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_number', models.IntegerField()),
                ('l_name', models.CharField(max_length=1024)),
                ('video', models.FileField(upload_to='videos')),
                ('l_description', models.CharField(blank=True, max_length=512, null=True)),
                ('for_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
            ],
        ),
        migrations.CreateModel(
            name='DashOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, default='#', max_length=512, null=True)),
                ('label', models.CharField(max_length=512)),
                ('method', models.CharField(blank=True, max_length=512, null=True)),
                ('icon', models.CharField(blank=True, default='insert_emoticon', max_length=512, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_name', models.CharField(max_length=512)),
                ('cr_description', models.CharField(max_length=1024)),
                ('cr_url', models.URLField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='course_resource')),
                ('for_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='for_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.course'),
        ),
    ]
