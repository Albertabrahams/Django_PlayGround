# Generated by Django 4.0.4 on 2022-05-18 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0005_student_register_date_student_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birt_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
