# Generated by Django 2.1.10 on 2019-07-29 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0032_addvendors'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddPurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('New', 'New'), ('Approved', 'Approved'), ('Fully Received', 'Fully Received'), ('Canceled', 'Canceled')], max_length=100)),
                ('req_num', models.IntegerField()),
                ('contact', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('commission', models.IntegerField()),
                ('e_duty', models.IntegerField()),
                ('carrier', models.CharField(choices=[('FedEx', 'FedEx'), ('UPS', 'UPS'), ('USPS', 'USPS'), ('DHL', 'DHL'), ('BlueDart', 'BlueDart')], max_length=100)),
                ('tracking_num', models.IntegerField()),
                ('ass_to', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=100)),
                ('bill_c', models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100)),
                ('shipp_c', models.CharField(choices=[('INDIA', 'INDIA'), ('UNITED STATES', 'UNITED STATES'), ('RUSSIA', 'RUSSIA'), ('CHINA', 'CHINA'), ('AUSTRALIA', 'AUSTRALIA'), ('FRANCE', 'FRANCE')], max_length=100)),
                ('b_a', models.CharField(max_length=100)),
                ('s_a', models.CharField(max_length=100)),
                ('b_postal_code', models.IntegerField()),
                ('s_postal_code', models.IntegerField()),
            ],
        ),
    ]
