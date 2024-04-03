# Generated by Django 5.0.3 on 2024-04-02 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_scheduleexams_school_group_alter_teacher_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
        migrations.AlterField(
            model_name='homework',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2024, 4, 2, 20, 34, 22, 690265)),
        ),
    ]