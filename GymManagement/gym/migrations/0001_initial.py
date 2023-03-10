# Generated by Django 3.1.3 on 2022-09-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=11)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=11)),
                ('unit', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=11)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('Plan', models.CharField(max_length=50)),
                ('Joindate', models.CharField(max_length=40)),
                ('Expiredate', models.CharField(max_length=40)),
                ('initialamount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('amount', models.CharField(max_length=11)),
                ('duration', models.CharField(max_length=10)),
            ],
        ),
    ]
