# Generated by Django 2.2.4 on 2019-09-03 20:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_eveonline_connector', '0002_evetoken_primary'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evetoken',
            unique_together={('user', 'primary')},
        ),
    ]
