# Generated by Django 4.2.4 on 2023-08-22 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldsplit_api', '0007_runs_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='runs',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 44, 40, 982506), editable=False),
        ),
    ]
