# Generated by Django 3.1 on 2020-08-14 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
