# Generated by Django 2.2.4 on 2019-12-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_eveonline_connector', '0008_auto_20191210_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eveclient',
            name='esi_sso_url',
            field=models.URLField(editable=False, max_length=2056),
        ),
    ]
