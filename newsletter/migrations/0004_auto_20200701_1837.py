# Generated by Django 3.0.7 on 2020-07-01 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20200701_1045'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterTemplate',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
