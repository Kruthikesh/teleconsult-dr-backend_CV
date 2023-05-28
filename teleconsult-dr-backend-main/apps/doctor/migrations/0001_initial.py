# Generated by Django 4.1.7 on 2023-04-30 10:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('record_id', models.UUIDField(default=uuid.uuid4, help_text='common primary key for all the tables', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('record_id', models.UUIDField(default=uuid.uuid4, help_text='common primary key for all the tables', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=512, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')])),
                ('specialisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='specialisation', to='doctor.specialisation')),
            ],
            options={
                'db_table': 'da_doctor',
                'abstract': False,
            },
        ),
    ]
