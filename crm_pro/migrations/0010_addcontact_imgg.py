# Generated by Django 2.1.10 on 2019-07-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0009_remove_addcontact_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcontact',
            name='imgg',
            field=models.ImageField(default=0, upload_to='pictures'),
            preserve_default=False,
        ),
    ]
