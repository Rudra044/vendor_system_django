# Generated by Django 5.0.4 on 2024-05-04 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='total_order',
            field=models.IntegerField(null=True),
        ),
    ]
