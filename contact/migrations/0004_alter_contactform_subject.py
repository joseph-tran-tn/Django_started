# Generated by Django 4.0 on 2021-09-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contactform_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
