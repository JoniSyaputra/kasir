# Generated by Django 4.1.2 on 2022-12-18 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='tahun_jabatan',
            new_name='tahun_kenaikan',
        ),
    ]