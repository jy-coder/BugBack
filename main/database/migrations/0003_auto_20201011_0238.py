# Generated by Django 3.1.2 on 2020-10-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20201011_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
