# Generated by Django 5.1.1 on 2024-10-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0010_resquestsupplier_addresssupplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresssupplier',
            name='complement',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Complemento'),
        ),
    ]
