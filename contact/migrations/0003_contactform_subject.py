# Generated by Django 4.0 on 2021-09-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactform_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
