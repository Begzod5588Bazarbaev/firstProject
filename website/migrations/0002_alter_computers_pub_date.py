# Generated by Django 4.1.4 on 2022-12-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computers',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
