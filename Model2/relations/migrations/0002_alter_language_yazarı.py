# Generated by Django 4.0.4 on 2022-05-18 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='yazarı',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='relations.creator'),
        ),
    ]
