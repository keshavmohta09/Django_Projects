# Generated by Django 2.1.10 on 2019-07-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0019_addcompaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOppurtunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oppo_name', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('org_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('close_date', models.DateField()),
                ('pipeline', models.CharField(choices=[('Standard', 'Standard')], max_length=100)),
                ('sales_stages', models.CharField(choices=[('New', 'New'), ('Requirements Gathering', 'Requirements Gathering'), ('Value Proposition', 'Value Proposition'), ('Negotiation', 'Negotiation'), ('Ready to close', 'Ready to close'), ('Closed won', 'Closed won')], max_length=100)),
                ('assigned_to', models.CharField(max_length=100)),
                ('lead_source', models.CharField(choices=[('Cold Call', 'Cold Call'), ('Refferal', 'Refferal'), ('World of mouth', 'World of mouth'), ('Website', 'Website'), ('Existing customer', 'Existing customer'), ('Direct Mail', 'Direct Mail'), ('Facebook', 'Facebook')], max_length=100)),
                ('type_b', models.CharField(choices=[('Existing Business', 'Existing Business'), ('New Business', 'New Business')], max_length=100)),
                ('probability', models.CharField(max_length=100)),
                ('camp_source', models.CharField(max_length=100)),
                ('revenue', models.IntegerField()),
                ('p_mail', models.EmailField(max_length=254)),
                ('lost_reason', models.CharField(choices=[('Price', 'Price'), ('Authority', 'Authority'), ('Timing', 'Timing'), ('Missing Feature', 'Missing Feature'), ('Usability', 'Usability'), ('No need', 'No need')], max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
