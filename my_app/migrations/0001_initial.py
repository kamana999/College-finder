# Generated by Django 3.0.2 on 2020-04-12 05:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryName',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_id', models.AutoField(primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('img', models.ImageField(upload_to='pic/')),
                ('website', models.URLField()),
                ('desc', models.TextField(blank=True)),
                ('avgrating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesName',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('course_duration', models.CharField(max_length=200)),
                ('course_fee', models.IntegerField(default=0)),
                ('elegibilty', models.CharField(max_length=200)),
                ('course_cat', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_app.CategoryName')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('exam_title', models.CharField(max_length=200)),
                ('exam_name', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=2000)),
                ('date_of_exam', models.DateField()),
                ('doc', models.DateTimeField(default=django.utils.timezone.now)),
                ('exam_eligiblity', models.TextField(max_length=2000)),
                ('age_limit', models.CharField(max_length=200)),
                ('syllabus', models.TextField(max_length=1000)),
                ('application_process', models.TextField(max_length=2000)),
                ('application_fee', models.CharField(max_length=500)),
                ('exam_center', models.CharField(max_length=1000)),
                ('mobile', models.IntegerField()),
                ('exam_website', models.URLField()),
                ('office_address', models.CharField(max_length=500)),
                ('exam_mode', models.CharField(max_length=200)),
                ('exam_duration', models.CharField(max_length=300)),
                ('application_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('release_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('s_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dp', models.ImageField(upload_to='pic/')),
                ('address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('status', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=200)),
                ('doc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeName',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_type', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.College')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.TypeName')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('rating', models.FloatField(default=0)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.College')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Student')),
            ],
        ),
        migrations.CreateModel(
            name='ExamCourse',
            fields=[
                ('ec_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CoursesName')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamCollege',
            fields=[
                ('eco_id', models.AutoField(primary_key=True, serialize=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.College')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='coursesname',
            name='course_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.TypeName'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('collegeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.College')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CoursesName')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='affiliated_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.University'),
        ),
        migrations.AddField(
            model_name='college',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.City'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.State'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ca_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CategoryName')),
                ('courseeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CoursesName')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.College')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.CoursesName')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Student')),
            ],
        ),
    ]