# Generated by Django 2.1.10 on 2019-07-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_pro', '0025_addservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddInvoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=100)),
                ('in_date', models.DateField()),
                ('due_date', models.DateField()),
                ('contact', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('s_order', models.CharField(max_length=100)),
                ('p_order', models.CharField(max_length=100)),
                ('assigned_to', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('s_duty', models.IntegerField()),
                ('p_duty', models.IntegerField()),
                ('oppo', models.CharField(max_length=100)),
                ('pro', models.CharField(max_length=100)),
                ('q_name', models.CharField(max_length=100)),
                ('r_to', models.CharField(max_length=100)),
                ('cbaf', models.CharField(max_length=100)),
                ('csaf', models.CharField(max_length=100)),
                ('bill_c', models.CharField(max_length=100)),
                ('shipp_c', models.CharField(max_length=100)),
                ('b_a', models.TextField()),
                ('s_a', models.TextField()),
                ('bpc', models.IntegerField()),
                ('spc', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
