# Generated by Django 2.1.10 on 2019-07-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0017_auto_20190723_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addorganization',
            name='billing_country',
            field=models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='addorganization',
            name='shipping_country',
            field=models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100),
        ),
    ]
