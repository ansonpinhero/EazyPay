# Generated by Django 2.0.1 on 2018-11-26 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_jobprofile_identify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobprofile',
            name='identify',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedjobs', to=settings.AUTH_USER_MODEL),
        ),
    ]
