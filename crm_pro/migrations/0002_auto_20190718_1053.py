# Generated by Django 2.1.10 on 2019-07-18 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addprojects',
            name='progress',
        ),
        migrations.RemoveField(
            model_name='addprojects',
            name='project_url',
        ),
    ]
