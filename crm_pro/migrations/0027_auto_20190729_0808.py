# Generated by Django 2.1.10 on 2019-07-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0026_addinvoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addinvoices',
            name='bill_c',
            field=models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='addinvoices',
            name='cbaf',
            field=models.CharField(choices=[('Organization', 'Organization'), ('Related To', 'Related To'), ('Shipping Address', 'Shipping Address')], max_length=100),
        ),
        migrations.AlterField(
            model_name='addinvoices',
            name='csaf',
            field=models.CharField(choices=[('Organization', 'Organization'), ('Related To', 'Related To'), ('Shipping Address', 'Shipping Address')], max_length=100),
        ),
        migrations.AlterField(
            model_name='addinvoices',
            name='shipp_c',
            field=models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100),
        ),
        migrations.AlterField(
            model_name='addinvoices',
            name='status',
            field=models.CharField(choices=[('Auto Created', 'Auto Created'), ('New', 'New'), ('Approved', 'Approved'), ('Partially Paid', 'Partially Paid'), ('Paid', 'Paid')], max_length=100),
        ),
    ]
