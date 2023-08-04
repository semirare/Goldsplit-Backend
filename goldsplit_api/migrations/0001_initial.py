# Generated by Django 4.2.4 on 2023-08-04 22:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Runs',
            fields=[
                ('run_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('game_name', models.CharField(max_length=200)),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Splits',
            fields=[
                ('split_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('split_name', models.CharField(max_length=200)),
                ('split_time', models.TimeField()),
                ('total_time', models.TimeField()),
                ('gold_time', models.TimeField()),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldsplit_api.runs')),
            ],
        ),
    ]
