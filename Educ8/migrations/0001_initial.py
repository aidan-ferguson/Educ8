# Generated by Django 2.1.5 on 2022-03-11 18:18

import Educ8.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseName', models.CharField(max_length=256, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(4)])),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=Educ8.models.generate_file_path)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educ8.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(1)])),
                ('question', models.CharField(max_length=1024, validators=[django.core.validators.MinLengthValidator(1)])),
                ('answer', models.CharField(max_length=1024, validators=[django.core.validators.MinLengthValidator(1)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educ8.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(max_length=32, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, validators=[django.core.validators.MinLengthValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(max_length=32, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, validators=[django.core.validators.MinLengthValidator(4)])),
            ],
        ),
        migrations.AddField(
            model_name='flashcard',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Educ8.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Educ8.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='Educ8.Student'),
        ),
    ]
