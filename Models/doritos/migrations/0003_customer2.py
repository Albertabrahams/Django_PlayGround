# Generated by Django 4.0.4 on 2022-05-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doritos', '0002_customer_rename_types_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('mature', models.BooleanField()),
            ],
        ),
    ]
