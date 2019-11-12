# Generated by Django 2.2.7 on 2019-11-07 20:46

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticky',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sticky',
            name='uuidu',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
    ]
