# Generated by Django 2.1 on 2018-01-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyTemplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='Active_IsDelete',
            field=models.IntegerField(default=0),
        ),
    ]