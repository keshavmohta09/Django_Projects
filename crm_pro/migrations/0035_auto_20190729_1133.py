# Generated by Django 2.1.10 on 2019-07-29 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0034_addpurchaseorder_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpurchaseorder',
            name='b_a',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='addpurchaseorder',
            name='s_a',
            field=models.TextField(),
        ),
    ]
